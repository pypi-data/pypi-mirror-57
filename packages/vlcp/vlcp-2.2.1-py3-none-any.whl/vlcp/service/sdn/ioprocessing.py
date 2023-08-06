'''
Created on 2016/4/13

:author: hubo
'''
from vlcp.service.sdn.flowbase import FlowBase
from vlcp.server.module import depend, ModuleNotification, call_api,api
import vlcp.service.sdn.ofpportmanager as ofpportmanager
import vlcp.service.sdn.ovsdbportmanager as ovsdbportmanager
import vlcp.service.kvdb.objectdb as objectdb
from vlcp.event.event import Event, withIndices, M_
from vlcp.event.runnable import RoutineContainer, RoutineException
from vlcp.config.config import defaultconfig
from vlcp.service.sdn.ofpmanager import FlowInitialize
from vlcp.utils.networkmodel import PhysicalPort, LogicalPort, PhysicalPortSet, LogicalPortSet, LogicalNetwork, \
    PhysicalNetwork,SubNet,RouterPort,VRouter, \
    PhysicalNetworkMap
from vlcp.utils.flowupdater import FlowUpdater

import itertools
from functools import partial
from contextlib import closing, suppress
from vlcp.utils.exceptions import WalkKeyNotRetrieved
from vlcp.protocol.openflow.openflow import OpenflowConnectionStateEvent

@withIndices('datapathid', 'vhost', 'connection', 'logicalportchanged', 'physicalportchanged',
                                                    'logicalnetworkchanged', 'physicalnetworkchanged')
class DataObjectChanged(Event):
    pass

class IDAssigner(object):
    def __init__(self):
        self._indices = {}
        self._revindices = {}
        # Reserve 0 and 0xffff
        self._revindices[0] = '<reserve0>'
        self._revindices[0xffff] = '<reserve65535>'
        self._lastindex = 1
    def assign(self, key):
        if key in self._indices:
            return self._indices[key]
        else:
            ind = self._lastindex
            while ind in self._revindices:
                ind += 1
                ind &= 0xffff
            self._revindices[ind] = key
            self._indices[key] = ind
            self._lastindex = ind + 1
            return ind
    def unassign(self, keys):
        for k in keys:
            ind = self._indices.pop(k, None)
            if ind is not None:
                del self._revindices[ind]
    def frozen(self):
        return dict(self._indices)

def _to32bitport(portno):
    if portno >= 0xff00:
        portno = 0xffff0000 | portno
    return portno


@withIndices('connection')
class FlowReadyEvent(Event):
    pass


class IOFlowUpdater(FlowUpdater):
    def __init__(self, connection, systemid, bridgename, parent):
        FlowUpdater.__init__(self, connection, (PhysicalPortSet.default_key(),),
                                            ('ioprocessing', connection),
                                            parent._logger)
        self._walkerdict = {PhysicalPortSet.default_key(): partial(self._physicalport_walker, _portnames={})}
        self._systemid = systemid
        self._bridgename = bridgename
        self._portnames = {}
        self._portids = {}
        self._currentportids = {}
        self._currentportnames = {}
        self._lastportids = {}
        self._lastportnames = {}
        self._lastnetworkids = {}
        self._networkids = IDAssigner()
        self._phynetworkids = IDAssigner()
        self._physicalnetworkids = {}
        self._logicalportkeys = set()
        self._physicalportkeys = set()
        self._logicalnetworkkeys = set()
        self._physicalnetworkkeys = set()
        self._original_initialkeys = []
        self._append_initialkeys = []
        self._parent = parent
        self._flows_sent = set()

    async def update_ports(self, ports, ovsdb_ports):
        """
        Called from main module to update port information
        """
        new_port_names = dict((p['name'], _to32bitport(p['ofport'])) for p in ovsdb_ports)
        new_port_ids = dict((p['id'], _to32bitport(p['ofport'])) for p in ovsdb_ports if p['id'])
        if new_port_names == self._portnames and new_port_ids == self._portids:
            return
        self._portnames.clear()
        self._portnames.update(new_port_names)
        self._portids.clear()
        self._portids.update(new_port_ids)

        logicalportkeys = [LogicalPort.default_key(id) for id in self._portids]

        self._original_initialkeys = logicalportkeys + [PhysicalPortSet.default_key()]
        self._initialkeys = tuple(itertools.chain(self._original_initialkeys, self._append_initialkeys))
        phy_walker = partial(self._physicalport_walker, _portnames=new_port_names)
        log_walker = partial(self._logicalport_walker, _portids=new_port_ids)
        self._walkerdict = dict(itertools.chain(
            ((PhysicalPortSet.default_key(),phy_walker),),
            ((lgportkey,log_walker) for lgportkey in logicalportkeys)
        ))
        self._portnames = new_port_names
        self._portids = new_port_ids
        await self.restart_walk()

    async def flowready(self, logicalnetworkid, physicalportid):
        # 1. Check the current updated flows
        # 2. Check the current logicalnetwork and physicalport
        # 3. Wait for:
        #    a. flow updated event
        #    b. data object change event
        #    c. connection down event

        flowready_matcher = FlowReadyEvent.createMatcher(self._connection)
        conn_down = self._connection.protocol.statematcher(self._connection)
        dataobjectchanged = DataObjectChanged.createMatcher(None, None, self._connection)
        while self._connection.connected:
            currentlognetid = dict((id, n) for n, id in self._lastlognets)
            currentphyportid = dict((id, (p, p.physicalnetwork)) for p, id in self._lastphyports)
            if (logicalnetworkid, physicalportid) in self._flows_sent:
                return True
            elif logicalnetworkid in currentlognetid and physicalportid in currentphyportid:
                conn_down = OpenflowConnectionStateEvent.createMatcher(None, None, OpenflowConnectionStateEvent.CONNECTION_DOWN, self._connection)
                await M_(dataobjectchanged, conn_down, flowready_matcher)
            else:
                return False
        return False

    def _logicalport_walker(self, key, value, walk, save, _portids):
        _, (id,) = LogicalPort._getIndices(key)
        if id not in _portids:
            return
        save(key)
        if value is None:
            return
        with suppress(WalkKeyNotRetrieved):
            lognet = walk(value.network.getkey())
            save(lognet.getkey())
            phynet = walk(lognet.physicalnetwork.getkey())
            save(phynet.getkey())
        if hasattr(value,"subnet"):
            with suppress(WalkKeyNotRetrieved):
                subnet = walk(value.subnet.getkey())
                save(subnet.getkey())
                if hasattr(subnet,"router"):
                    routerport = walk(subnet.router.getkey())
                    save(routerport.getkey())
                    if hasattr(routerport,"router"):
                        router = walk(routerport.router.getkey())
                        save(router.getkey())
                        if router.interfaces.dataset():
                            for weakobj in router.interfaces.dataset():
                                with suppress(WalkKeyNotRetrieved):
                                    weakrouterport = walk(weakobj.getkey())
                                    save(weakrouterport.getkey())
                                    s = walk(weakrouterport.subnet.getkey())
                                    save(s.getkey())
                                    lgnet = walk(s.network.getkey())
                                    save(lgnet.getkey())
    def _physicalport_walker(self, key, value, walk, save, _portnames):
        save(key)
        if value is None:
            return
        physet = value.set
        for name in _portnames:
            phyports = physet.find(PhysicalPort, self._connection.protocol.vhost, self._systemid, self._bridgename, name)
            # There might be more than one match physical port rule for one port, pick the most specified one
            namedict = {}
            for p in phyports:
                _, inds = PhysicalPort._getIndices(p.getkey())
                name = inds[-1]
                ind_key = [i != '%' for i in inds]
                if name != '%':
                    if name in namedict:
                        if namedict[name][0] < ind_key:
                            namedict[name] = (ind_key, p)
                    else:
                        namedict[name] = (ind_key, p)
            phyports = [v[1] for v in namedict.values()]
            for p in phyports:
                with suppress(WalkKeyNotRetrieved):
                    phyp = walk(p.getkey())
                    save(phyp.getkey())
                    phynet = walk(phyp.physicalnetwork.getkey())
                    save(phynet.getkey())
                    if self._parent.enable_router_forward:
                        phynetmap = walk(PhysicalNetworkMap.default_key(phynet.id))
                        save(phynetmap.getkey())
                        for weak_lgnet in  phynetmap.logicnetworks.dataset():
                            with suppress(WalkKeyNotRetrieved):
                                lgnet = walk(weak_lgnet.getkey())
                                save(lgnet.getkey())

    def reset_initialkeys(self,keys,values):

        subnetkeys = [k for k,v in zip(keys,values) if v is not None and not v.isdeleted() and
                      v.isinstance(SubNet)]
        routerportkeys = [k for k,v in zip(keys,values) if v is not None and not v.isdeleted() and
                          v.isinstance(RouterPort)]
        portkeys = [k for k,v in zip(keys,values) if v is not None and not v.isdeleted() and
                    v.isinstance(VRouter)]
        self._append_initialkeys = subnetkeys + routerportkeys + portkeys
        self._initialkeys = tuple(itertools.chain(self._original_initialkeys, self._append_initialkeys))

    async def walkcomplete(self, keys, values):
        conn = self._connection
        dpid = conn.openflow_datapathid
        vhost = conn.protocol.vhost
        _currentportids = dict(self._portids)
        _currentportnames = dict(self._portnames)
        updated_data = {}
        current_data = {}
        for cls, name, idg, assigner in ((LogicalPort, '_logicalportkeys', lambda x: _currentportids.get(x.id), None),
                                 (PhysicalPort, '_physicalportkeys', lambda x: _currentportnames.get(x.name), None),
                                 (LogicalNetwork, '_logicalnetworkkeys', lambda x: self._networkids.assign(x.getkey()), self._networkids),
                                 (PhysicalNetwork, '_physicalnetworkkeys', lambda x: self._phynetworkids.assign(x.getkey()), self._phynetworkids),
                                 ):
            objs = [v for v in values if v is not None and not v.isdeleted() and v.isinstance(cls)]
            cv = [(o, oid) for o,oid in ((o, idg(o)) for o in objs) if oid is not None]
            objkeys = set([v.getkey() for v,_ in cv])
            oldkeys = getattr(self, name)
            current_data[cls] = cv
            if objkeys != oldkeys:
                if assigner is not None:
                    assigner.unassign(oldkeys.difference(objkeys))
                setattr(self, name, objkeys)
                updated_data[cls] = True
        if updated_data:
            await self.wait_for_send(DataObjectChanged(dpid, vhost, conn, LogicalPort in updated_data,
                                                                            PhysicalPort in updated_data,
                                                                            LogicalNetwork in updated_data,
                                                                            PhysicalNetwork in updated_data,
                                                                            current = (current_data.get(LogicalPort),
                                                                                       current_data.get(PhysicalPort),
                                                                                       current_data.get(LogicalNetwork),
                                                                                       current_data.get(PhysicalNetwork))))
        self._lastlognets = current_data.get(LogicalNetwork)
        self._lastphyports = current_data.get(PhysicalPort)
        self._currentportids = _currentportids
        self._currentportnames = _currentportnames

    async def updateflow(self, connection, addvalues, removevalues, updatedvalues):
        # We must do these in order, each with a batch:
        # 1. Remove flows
        # 2. Remove groups
        # 3. Add groups, modify groups
        # 4. Add flows, modify flows
        try:
            cmds = []
            ofdef = connection.openflowdef
            vhost = connection.protocol.vhost
            input_table = self._parent._gettableindex('ingress', vhost)
            input_next = self._parent._getnexttable('', 'ingress', vhost = vhost)
            output_table = self._parent._gettableindex('egress', vhost)
            # Cache all IDs, save them into last. We will need them for remove.
            _lastportids = self._lastportids
            _lastportnames = self._lastportnames
            _lastnetworkids = self._lastnetworkids
            _portids = dict(self._currentportids)
            _portnames = dict(self._currentportnames)
            _networkids = self._networkids.frozen()
            exist_objs = dict((obj.getkey(), obj) for obj in self._savedresult if obj is not None and not obj.isdeleted())
            # We must generate actions from network driver
            phyportset = [obj for obj in self._savedresult if obj is not None and not obj.isdeleted() and obj.isinstance(PhysicalPort)]
            phynetset = [obj for obj in self._savedresult if obj is not None and not obj.isdeleted() and obj.isinstance(PhysicalNetwork)]
            lognetset = [obj for obj in self._savedresult if obj is not None and not obj.isdeleted() and obj.isinstance(LogicalNetwork)]
            logportset = [obj for obj in self._savedresult if obj is not None and not obj.isdeleted() and obj.isinstance(LogicalPort)]
            # If a port is both a logical port and a physical port, flows may conflict.
            # Remove the port from dictionary if it is duplicated.
            logportofps = set(_portids[lp.id] for lp in logportset if lp.id in _portids)
            _portnames = dict((n,v) for n,v in _portnames.items() if v not in logportofps)
            self._lastportids = _portids
            self._lastportnames = _portnames
            self._lastnetworkids = _networkids
            # Group current ports by network for further use
            phyportdict = {}
            for p in phyportset:
                phyportdict.setdefault(p.physicalnetwork, []).append(p)
            lognetdict = {}
            for n in lognetset:
                lognetdict.setdefault(n.physicalnetwork, []).append(n)
            logportdict = {}
            for p in logportset:
                logportdict.setdefault(p.network, []).append(p)
            allapis = []
            # Updated networks when:
            # 1. Network is updated
            # 2. Physical network of this logical network is updated
            # 3. Logical port is added or removed from the network
            # 4. Physical port is added or removed from the physical network
            group_updates = set([obj for obj in updatedvalues if obj.isinstance(LogicalNetwork)])
            group_updates.update(obj.network for obj in addvalues if obj.isinstance(LogicalPort))
            #group_updates.update(obj.network for obj in updatedvalues if obj.isinstance(LogicalPort))
            group_updates.update(exist_objs[obj.network.getkey()] for obj in removevalues if obj.isinstance(LogicalPort) and obj.network.getkey() in exist_objs)
            updated_physicalnetworks = set(obj for obj in updatedvalues if obj.isinstance(PhysicalNetwork))
            updated_physicalnetworks.update(p.physicalnetwork for p in addvalues if p.isinstance(PhysicalPort))
            updated_physicalnetworks.update(exist_objs[p.physicalnetwork.getkey()] for p in removevalues if p.isinstance(PhysicalPort) and p.physicalnetwork.getkey() in exist_objs)
            updated_physicalnetworks.update(p.physicalnetwork for p in updatedvalues if p.isinstance(PhysicalPort))
            group_updates.update(lnet for pnet in updated_physicalnetworks
                                 if pnet in lognetdict
                                 for lnet in lognetdict[pnet])
            _flows_sent = set()
            for pnet in phynetset:
                if pnet in lognetdict and pnet in phyportdict:
                    for lognet in lognetdict[pnet]:
                        netid = _networkids.get(lognet.getkey())
                        if netid is not None:
                            for p in phyportdict[pnet]:
                                if lognet in addvalues or lognet in group_updates or p in addvalues or p in updatedvalues:
                                    pid = _portnames.get(p.name)
                                    if pid is not None:
                                        async def subr(lognet, p, netid, pid):
                                            try:
                                                r = await call_api(self, 'public', 'createioflowparts', {'connection': connection,
                                                                                                       'logicalnetwork': lognet,
                                                                                                       'physicalport': p,
                                                                                                       'logicalnetworkid': netid,
                                                                                                       'physicalportid': pid})
                                            except Exception:
                                                self._parent._logger.warning("Create flow parts failed for %r and %r", lognet, p, exc_info = True)
                                                return None
                                            else:
                                                _flows_sent.add((netid, pid))
                                                return ((lognet, p), r)
                                        allapis.append(subr(lognet, p, netid, pid))
            flowparts_result = await self.execute_all(allapis)
            flowparts = dict(r for r in flowparts_result if r is not None)
            if connection.protocol.disablenxext:
                # Nicira extension is disabled, use metadata instead
                # 64-bit metadata is used as:
                # | 16-bit input network | 16-bit output network | 16-bit reserved | 16-bit output port |
                # When first initialized, input network = output network = Logical Network no.
                # output port = OFPP_ANY, reserved bits are 0x0000
                # Currently used reserved bits:
                # left-most (offset = 15, mask = 0x8000): allow output to IN_PORT
                # offset = 14, mask = 0x4000: 1 if is IN_PORT is a logical port, 0 else
                # right-most (offset = 0, mask = 0x0001): VXLAN learned
                def create_input_instructions(lognetid, extra_actions, is_logport):
                    lognetid = (lognetid & 0xffff)
                    instructions = [ofdef.ofp_instruction_write_metadata(
                                        metadata = (lognetid << 48) | (lognetid << 32) | ((0x4000 if is_logport else 0) << 16) | (ofdef.OFPP_ANY & 0xffff),
                                        metadata_mask = 0xffffffffffffffff
                                    ),
                                    ofdef.ofp_instruction_goto_table(table_id = input_next)
                                    ]
                    if extra_actions:
                        instructions.insert(0, ofdef.ofp_instruction_actions(actions = list(extra_actions)))
                    return instructions
                def create_output_oxm(lognetid, portid, in_port = False):
                    r = [ofdef.create_oxm(ofdef.OXM_OF_METADATA_W, (portid & 0xFFFF) | (0x80000000 if in_port else 0) | ((lognetid & 0xFFFF) << 32), 0x0000FFFF8000FFFF)]
                    if in_port:
                        r.append(ofdef.create_oxm(ofdef.OXM_OF_IN_PORT, portid))
                    return r
            else:
                # With nicira extension, we store input network, output network and output port in REG4, REG5 and REG6
                # REG7 is used as the reserved bits
                def create_input_instructions(lognetid, extra_actions, is_logport):
                    lognetid = (lognetid & 0xffff)
                    return [ofdef.ofp_instruction_actions(actions = [
                                    ofdef.ofp_action_set_field(
                                            field = ofdef.create_oxm(ofdef.NXM_NX_REG4, lognetid)
                                            ),
                                    ofdef.ofp_action_set_field(
                                            field = ofdef.create_oxm(ofdef.NXM_NX_REG5, lognetid)
                                            ),
                                    ofdef.ofp_action_set_field(
                                            field = ofdef.create_oxm(ofdef.NXM_NX_REG6, ofdef.OFPP_ANY)
                                            ),
                                    ofdef.ofp_action_set_field(
                                            field = ofdef.create_oxm(ofdef.NXM_NX_REG7, (0x4000 if is_logport else 0))
                                            )
                                ] + list(extra_actions)),
                            ofdef.ofp_instruction_goto_table(table_id = input_next)
                            ]
                def create_output_oxm(lognetid, portid, in_port = False):
                    r = [ofdef.create_oxm(ofdef.NXM_NX_REG5, lognetid),
                            ofdef.create_oxm(ofdef.NXM_NX_REG6, portid),
                            ofdef.create_oxm(ofdef.NXM_NX_REG7_W, 0x8000 if in_port else 0, 0x8000)]
                    if in_port:
                        r.append(ofdef.create_oxm(ofdef.OXM_OF_IN_PORT, portid))
                    return r
            for obj in removevalues:
                if obj.isinstance(LogicalPort):
                    ofport = _lastportids.get(obj.id)
                    if ofport is not None:
                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                 ofport
                                                                                 )])
                                                       ))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofport,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm()))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_IN_PORT,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                    ofdef.create_oxm(ofdef.OXM_OF_IN_PORT, ofport)])))
                elif obj.isinstance(PhysicalPort):
                    ofport = _lastportnames.get(obj.name)
                    if ofport is not None:
                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                 ofport
                                                                                 )])
                                                       ))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       cookie = 0x0001000000000000 | ((ofport & 0xffff) << 16),
                                                       cookie_mask = 0xffffffffffff0000,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm()))
                elif obj.isinstance(LogicalNetwork):
                    groupid = _lastnetworkids.get(obj.getkey())
                    if groupid is not None:
                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                       cookie = 0x0001000000000000 | groupid,
                                                       cookie_mask = 0xffffffffffffffff,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm()
                                                       ))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       cookie = 0x0001000000000000 | groupid,
                                                       cookie_mask = 0xffff00000000ffff,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm()
                                                       ))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(groupid, ofdef.OFPP_ANY))
                                                       ))
            # Never use flow mod to update an input flow of physical port, because the input_oxm may change.
            for obj in updatedvalues:
                if obj.isinstance(PhysicalPort):
                    ofport = _portnames.get(obj.name)
                    if ofport is not None:
                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                 ofport
                                                                                 )])
                                                       ))
                elif obj.isinstance(LogicalNetwork):
                    groupid = _networkids.get(obj.getkey())
                    if groupid is not None:
                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                       cookie = 0x0001000000000000 | groupid,
                                                       cookie_mask = 0xffffffffffffffff,
                                                       command = ofdef.OFPFC_DELETE,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm()
                                                       ))
                elif obj.isinstance(PhysicalNetwork):
                    if obj in phyportdict:
                        for p in phyportdict[obj]:
                            ofport = _portnames.get(p.name)
                            if ofport is not None and p not in addvalues and p not in updatedvalues:
                                cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                               command = ofdef.OFPFC_DELETE,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                        ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                         ofport
                                                                                         )])
                                                               ))
            await self.execute_commands(connection, cmds)
            del cmds[:]
            for obj in removevalues:
                if obj.isinstance(LogicalNetwork):
                    groupid = _lastnetworkids.get(obj.getkey())
                    if groupid is not None:
                        cmds.append(ofdef.ofp_group_mod(command = ofdef.OFPGC_DELETE,
                                                        type = ofdef.OFPGT_ALL,
                                                        group_id = groupid
                                                        ))
            await self.execute_commands(connection, cmds)
            del cmds[:]
            disablechaining = connection.protocol.disablechaining
            created_groups = {}
            def create_buckets(obj, groupid):
                # Generate buckets
                buckets = [ofdef.ofp_bucket(actions=[ofdef.ofp_action_output(port = _portids[p.id])])
                           for p in logportdict[obj]
                           if p.id in _portids] if obj in logportdict else []
                allactions = [ofdef.ofp_action_output(port = _portids[p.id])
                              for p in logportdict[obj]
                              if p.id in _portids] if obj in logportdict else []
                disablegroup = False
                if obj.physicalnetwork in phyportdict:
                    for p in phyportdict[obj.physicalnetwork]:
                        if (obj, p) in flowparts:
                            fp = flowparts[(obj,p)]
                            allactions.extend(fp[3])
                            if disablechaining and not disablegroup and any(a.type == ofdef.OFPAT_GROUP for a in fp[3]):
                                # We cannot use chaining. We use a long action list instead, and hope there is no conflicts
                                disablegroup = True
                            else:
                                buckets.append(ofdef.ofp_bucket(actions=list(fp[3])))
                if disablegroup:
                    created_groups[groupid] = allactions
                else:
                    created_groups[groupid] = [ofdef.ofp_action_group(group_id = groupid)]
                return buckets
            for obj in addvalues:
                if obj.isinstance(LogicalNetwork):
                    groupid = _networkids.get(obj.getkey())
                    if groupid is not None:
                        cmds.append(ofdef.ofp_group_mod(command = ofdef.OFPGC_ADD,
                                                        type = ofdef.OFPGT_ALL,
                                                        group_id = groupid,
                                                        buckets = create_buckets(obj, groupid)
                                                        ))
            for obj in group_updates:
                groupid = _networkids.get(obj.getkey())
                if groupid is not None:
                    cmds.append(ofdef.ofp_group_mod(command = ofdef.OFPGC_MODIFY,
                                                    type = ofdef.OFPGT_ALL,
                                                    group_id = groupid,
                                                    buckets = create_buckets(obj, groupid)
                                                    ))
            await self.execute_commands(connection, cmds)
            del cmds[:]
            # There are 5 kinds of flows:
            # 1. in_port = (Logical Port)
            # 2. in_port = (Physical_Port), network = (Logical_Network)
            # 3. out_port = (Logical Port)
            # 4. out_port = (Physical_Port), network = (Logical_Network)
            # 5. out_port = OFPP_ANY, network = (Logical_Network)
            for obj in addvalues:
                if obj.isinstance(LogicalPort):
                    ofport = _portids.get(obj.id)
                    lognetid = _networkids.get(obj.network.getkey())
                    if ofport is not None and lognetid is not None:
                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                       command = ofdef.OFPFC_ADD,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                 ofport
                                                                                 )]),
                                                       instructions = create_input_instructions(lognetid, [], True)
                                                       ))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       command = ofdef.OFPFC_ADD,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport)),
                                                       instructions = [ofdef.ofp_instruction_actions(actions = [
                                                                    ofdef.ofp_action_output(port = ofport)
                                                                    ])]
                                                       ))
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       command = ofdef.OFPFC_ADD,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, True)),
                                                       instructions = [ofdef.ofp_instruction_actions(actions = [
                                                                    ofdef.ofp_action_output(port = ofdef.OFPP_IN_PORT)
                                                                    ])]
                                                       ))
            # Ignore update of logical port
            # Physical port:
            for obj in addvalues:
                if obj.isinstance(PhysicalPort):
                    ofport = _portnames.get(obj.name)
                    if ofport is not None and obj.physicalnetwork in lognetdict:
                        for lognet in lognetdict[obj.physicalnetwork]:
                            lognetid = _networkids.get(lognet.getkey())
                            if lognetid is not None and (lognet, obj) in flowparts:
                                input_oxm, input_actions, output_actions, _, output_actions2 = flowparts[(lognet, obj)]
                                cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                               cookie = 0x0001000000000000 | lognetid,
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                        ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                         ofport
                                                                                         )] + list(input_oxm)),
                                                               instructions = create_input_instructions(lognetid, input_actions, False)
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, False)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions))]
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, True)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions2))]
                                                               ))
            for lognet in addvalues:
                if lognet.isinstance(LogicalNetwork):
                    lognetid = _networkids.get(lognet.getkey())
                    if lognetid is not None and lognet.physicalnetwork in phyportdict:
                        for obj in phyportdict[lognet.physicalnetwork]:
                            ofport = _portnames.get(obj.name)
                            if ofport is not None and (lognet, obj) in flowparts and obj not in addvalues:
                                input_oxm, input_actions, output_actions, _, output_actions2 = flowparts[(lognet, obj)]
                                cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                               cookie = 0x0001000000000000 | lognetid,
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                        ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                         ofport
                                                                                         )] + input_oxm),
                                                               instructions = create_input_instructions(lognetid, input_actions, False)
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, False)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions))]
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, True)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions2))]
                                                               ))
            for obj in updatedvalues:
                if obj.isinstance(PhysicalPort):
                    ofport = _portnames.get(obj.name)
                    if ofport is not None and obj.physicalnetwork in lognetdict:
                        for lognet in lognetdict[obj.physicalnetwork]:
                            lognetid = _networkids.get(lognet.getkey())
                            if lognetid is not None and (lognet, obj) in flowparts and not lognet in addvalues:
                                input_oxm, input_actions, output_actions, _, output_actions2 = flowparts[(lognet, obj)]
                                cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                               cookie = 0x0001000000000000 | lognetid,
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                        ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                         ofport
                                                                                         )] + input_oxm),
                                                               instructions = create_input_instructions(lognetid, input_actions, False)
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_MODIFY,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, False)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions))]
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_MODIFY,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, True)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions2))]
                                                               ))
            for lognet in updatedvalues:
                if lognet.isinstance(LogicalNetwork):
                    lognetid = _networkids.get(lognet.getkey())
                    if lognetid is not None and lognet.physicalnetwork in phyportdict:
                        for obj in phyportdict[lognet.physicalnetwork]:
                            ofport = _portnames.get(obj.name)
                            if ofport is not None and (lognet, obj) in flowparts and obj not in addvalues and obj not in updatedvalues:
                                input_oxm, input_actions, output_actions, _, output_actions2 = flowparts[(lognet, obj)]
                                cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                               cookie = 0x0001000000000000 | lognetid,
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_ADD,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                        ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                         ofport
                                                                                         )] + input_oxm),
                                                               instructions = create_input_instructions(lognetid, input_actions, False)
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_MODIFY,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions))]
                                                               ))
                                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                               cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                               cookie_mask = 0xffffffffffffffff,
                                                               command = ofdef.OFPFC_MODIFY,
                                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                                               out_port = ofdef.OFPP_ANY,
                                                               out_group = ofdef.OFPG_ANY,
                                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, True)),
                                                               instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                            list(output_actions2))]
                                                               ))
            # Physical network is updated
            for pnet in updatedvalues:
                if pnet.isinstance(PhysicalNetwork) and pnet in lognetdict:
                    for lognet in lognetdict[pnet]:
                        if lognet.isinstance(LogicalNetwork):
                            lognetid = _networkids.get(lognet.getkey())
                            if lognetid is not None and lognet not in updatedvalues and lognet not in addvalues and lognet.physicalnetwork in phyportdict:
                                for obj in phyportdict[lognet.physicalnetwork]:
                                    ofport = _portnames.get(obj.name)
                                    if ofport is not None and (lognet, obj) in flowparts and obj not in addvalues and obj not in updatedvalues:
                                        input_oxm, input_actions, output_actions, _, output_actions2 = flowparts[(lognet, obj)]
                                        cmds.append(ofdef.ofp_flow_mod(table_id = input_table,
                                                                       cookie = 0x0001000000000000 | lognetid,
                                                                       cookie_mask = 0xffffffffffffffff,
                                                                       command = ofdef.OFPFC_ADD,
                                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                                       out_port = ofdef.OFPP_ANY,
                                                                       out_group = ofdef.OFPG_ANY,
                                                                       match = ofdef.ofp_match_oxm(oxm_fields = [
                                                                                ofdef.create_oxm(ofdef.OXM_OF_IN_PORT,
                                                                                                 ofport
                                                                                                 )] + input_oxm),
                                                                       instructions = create_input_instructions(lognetid, input_actions, False)
                                                                       ))
                                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                                       cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                                       cookie_mask = 0xffffffffffffffff,
                                                                       command = ofdef.OFPFC_MODIFY,
                                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                                       out_port = ofdef.OFPP_ANY,
                                                                       out_group = ofdef.OFPG_ANY,
                                                                       match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport)),
                                                                       instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                                    list(output_actions))]
                                                                       ))
                                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                                       cookie = 0x0001000000000000 | lognetid | ((ofport & 0xffff) << 16),
                                                                       cookie_mask = 0xffffffffffffffff,
                                                                       command = ofdef.OFPFC_MODIFY,
                                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                                       out_port = ofdef.OFPP_ANY,
                                                                       out_group = ofdef.OFPG_ANY,
                                                                       match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofport, True)),
                                                                       instructions = [ofdef.ofp_instruction_actions(actions = 
                                                                                    list(output_actions2))]
                                                                       ))
            # Logical network broadcast
            for lognet in addvalues:
                if lognet.isinstance(LogicalNetwork):
                    lognetid = _networkids.get(lognet.getkey())
                    if lognetid is not None and lognetid in created_groups:
                        cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                                       command = ofdef.OFPFC_ADD,
                                                       priority = ofdef.OFP_DEFAULT_PRIORITY,
                                                       buffer_id = ofdef.OFP_NO_BUFFER,
                                                       out_port = ofdef.OFPP_ANY,
                                                       out_group = ofdef.OFPG_ANY,
                                                       match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofdef.OFPP_ANY)),
                                                       instructions = [ofdef.ofp_instruction_actions(actions =
                                                                            created_groups.pop(lognetid))]
                                                       ))
            for lognetid, actions in created_groups.items():
                cmds.append(ofdef.ofp_flow_mod(table_id = output_table,
                                               command = ofdef.OFPFC_ADD,
                                               priority = ofdef.OFP_DEFAULT_PRIORITY,
                                               buffer_id = ofdef.OFP_NO_BUFFER,
                                               out_port = ofdef.OFPP_ANY,
                                               out_group = ofdef.OFPG_ANY,
                                               match = ofdef.ofp_match_oxm(oxm_fields = create_output_oxm(lognetid, ofdef.OFPP_ANY)),
                                               instructions = [ofdef.ofp_instruction_actions(actions = actions)]
                                               ))                
            # Ignore logical network update
            await self.execute_commands(connection, cmds)
            self._flows_sent = _flows_sent
            await self.wait_for_send(FlowReadyEvent(self._connection))

        except Exception:
            self._parent._logger.warning("Update flow for connection %r failed with exception", connection, exc_info = True)
            # We don't want the whole flow update stops, so ignore the exception and continue
    
@defaultconfig
@depend(ofpportmanager.OpenflowPortManager, ovsdbportmanager.OVSDBPortManager, objectdb.ObjectDB)
class IOProcessing(FlowBase):
    "Ingress and Egress processing"
    _tablerequest = (("ingress", (), ''),
                     ("egress", ("ingress",),''))
    # vHost map from OpenFlow vHost to OVSDB vHost. If the OpenFlow vHost is not found in this map,
    # it will map to the default OVSDB vHost ('')
    _default_vhostmap = {}
    # Enable forwarding in this server, so it becomes a forwarding node (also known as a N/S gateway)
    _default_enable_router_forward = False

    def __init__(self, server):
        FlowBase.__init__(self, server)
        self.apiroutine = RoutineContainer(self.scheduler)
        self.apiroutine.main = self._main
        self.routines.append(self.apiroutine)
        self._flowupdaters = {}
        self._portchanging = set()
        self._portchanged = set()
        self.createAPI(api(self.flowready, self.apiroutine))

    async def flowready(self, connection, logicalnetworkid, physicalportid):
        """
        Wait until flows are sent to switch

        :param connection: Openflow connection
        :param logicalnetworkid: logical network id (integer)
        :param physicalportid: physical port id (integer)
        :return: If connection/network/port not exists, return False, else return True
        """
        if connection not in self._flowupdaters:
            return False
        else:
            return await self._flowupdaters[connection].flowready(logicalnetworkid, physicalportid)

    async def _main(self):
        flow_init = FlowInitialize.createMatcher(_ismatch = lambda x: self.vhostbind is None or x.vhost in self.vhostbind)
        port_change = ModuleNotification.createMatcher("openflowportmanager", "update", _ismatch = lambda x: self.vhostbind is None or x.vhost in self.vhostbind)
        while True:
            e, m = await M_(flow_init, port_change)
            c = e.connection
            if m is flow_init:
                self.apiroutine.subroutine(self._init_conn(c))
            else:
                if e.reason == 'disconnected':
                    self.apiroutine.subroutine(self._remove_conn(c))
                else:
                    self.apiroutine.subroutine(self._portchange(c))

    async def _init_conn(self, conn):
        # Default drop
        await conn.protocol.batch((conn.openflowdef.ofp_flow_mod(table_id = self._gettableindex("ingress", conn.protocol.vhost),
                                                           command = conn.openflowdef.OFPFC_ADD,
                                                           priority = 0,
                                                           buffer_id = conn.openflowdef.OFP_NO_BUFFER,
                                                           match = conn.openflowdef.ofp_match_oxm(),
                                                           instructions = [conn.openflowdef.ofp_instruction_actions(
                                                                            type = conn.openflowdef.OFPIT_CLEAR_ACTIONS
                                                                            )]
                                                           ),
                                      conn.openflowdef.ofp_flow_mod(table_id = self._gettableindex("egress", conn.protocol.vhost),
                                                           command = conn.openflowdef.OFPFC_ADD,
                                                           priority = 0,
                                                           buffer_id = conn.openflowdef.OFP_NO_BUFFER,
                                                           match = conn.openflowdef.ofp_match_oxm(),
                                                           instructions = [conn.openflowdef.ofp_instruction_actions(
                                                                            type = conn.openflowdef.OFPIT_CLEAR_ACTIONS
                                                                            )]
                                                           )), conn, self.apiroutine)
        if conn in self._flowupdaters:
            self._flowupdaters[conn].close()
        datapath_id = conn.openflow_datapathid
        ovsdb_vhost = self.vhostmap.get(conn.protocol.vhost, "")
        bridgename, systemid, _ = await call_api(self.apiroutine, 'ovsdbmanager', 'waitbridgeinfo',
                                                 {'datapathid': datapath_id,
                                                  'vhost': ovsdb_vhost})
        new_updater = IOFlowUpdater(conn, systemid, bridgename, self)
        self._flowupdaters[conn] = new_updater
        new_updater.start()
        await self._portchange(conn)

    async def _remove_conn(self, conn):
        # Do not need to modify flows
        if conn in self._flowupdaters:
            self._flowupdaters[conn].close()
            del self._flowupdaters[conn]

    async def _portchange(self, conn):
        # Do not re-enter
        if conn in self._portchanging:
            self._portchanged.add(conn)
            return
        self._portchanging.add(conn)
        last_portno = set()
        try:
            while True:
                self._portchanged.discard(conn)
                flow_updater = self._flowupdaters.get(conn)
                if flow_updater is None:
                    break
                if not conn.connected:
                    break
                datapath_id = conn.openflow_datapathid
                ovsdb_vhost = self.vhostmap.get(conn.protocol.vhost, "")
                ovsdb_update_event_matcher = ModuleNotification.createMatcher(
                                                "ovsdbportmanager",
                                                "update",
                                                _ismatch = lambda x: x.vhost == ovsdb_vhost and x.datapathid == datapath_id)
                ovsdb_updated = False
                def _ovsdb_update_callback(event, matcher):
                    nonlocal ovsdb_updated
                    ovsdb_updated = True
                ports, ovsdb_ports = \
                    await self.apiroutine.with_callback( 
                                    self.apiroutine.execute_all(
                                                    [call_api(self.apiroutine, 'openflowportmanager', 'getports', {'datapathid': datapath_id,
                                                                                            'vhost': conn.protocol.vhost}),
                                                     call_api(self.apiroutine, 'ovsdbportmanager', 'getports', {'datapathid': datapath_id,
                                                                                                  'vhost': ovsdb_vhost})]),
                                    _ovsdb_update_callback,
                                    ovsdb_update_event_matcher
                                )
                if conn in self._portchanged or ovsdb_updated:
                    # Retrieve again
                    continue
                if not conn.connected:
                    self._portchanged.discard(conn)
                    return
                ovsdb_port_dict = {p['ofport']: p for p in ovsdb_ports}
                # Choose the intersection of ports from two sources
                port_pairs = [(p, ovsdb_port_dict[p.port_no & 0xffff])
                              for p in ports
                              if (p.port_no & 0xffff) in ovsdb_port_dict]
                current_portno = {p.port_no for p, _ in port_pairs}
                # Get again to prevent concurrent problems
                flow_updater = self._flowupdaters.get(conn)
                if flow_updater is None:
                    break
                if not conn.connected:
                    break
                if conn in self._portchanged or ovsdb_updated:
                    continue
                # If all openflow ports have their OVSDB ports, we are in sync and can exit
                if all((p.port_no & 0xffff) in ovsdb_port_dict for p in ports):
                    if current_portno != last_portno:
                        if port_pairs:
                            await self.apiroutine.with_callback(
                                        flow_updater.update_ports(*zip(*port_pairs)),
                                        _ovsdb_update_callback,
                                        ovsdb_update_event_matcher
                                    )
                        else:
                            await self.apiroutine.with_callback(
                                        flow_updater.update_ports((), ()),
                                        _ovsdb_update_callback,
                                        ovsdb_update_event_matcher
                                    )
                    break
                else:
                    # Partially update
                    if current_portno and current_portno != last_portno:
                        if port_pairs:
                            await self.apiroutine.with_callback(
                                        flow_updater.update_ports(*zip(*port_pairs)),
                                        _ovsdb_update_callback,
                                        ovsdb_update_event_matcher
                                    )
                        else:
                            await self.apiroutine.with_callback(
                                        flow_updater.update_ports((), ()),
                                        _ovsdb_update_callback,
                                        ovsdb_update_event_matcher
                                    )
                        last_portno = current_portno                    
                    # Some openflow ports do not have OVSDB information, this may be caused
                    # by:
                    # 1. A port is added to OpenFlow, but not yet retrieved from OVSDB
                    # 2. A port is deleted from OVSDB, but not yet updated in OpenFlow
                    # 3. Other synchronization problem
                    port_change = ModuleNotification.createMatcher("openflowportmanager", "update",
                                                                   _ismatch = lambda x: x.connection == conn)
                    conndown = conn.protocol.statematcher(conn)
                    timeout, _, m = await self.apiroutine.wait_with_timeout(5,
                                                                            port_change,
                                                                            ovsdb_update_event_matcher,
                                                                            conndown)
                    if timeout:
                        self._logger.warning('OpenFlow ports may not be synchronized. Try resync...')
                        # Connection is up but ports are not synchronized, try resync
                        await self.apiroutine.execute_all([call_api(self.apiroutine, 'openflowportmanager', 'resync',
                                                                     {'datapathid': datapath_id,
                                                                      'vhost': conn.protocol.vhost}),
                                                           call_api(self.apiroutine, 'ovsdbportmanager', 'resync',
                                                                     {'datapathid': datapath_id,
                                                                      'vhost': ovsdb_vhost})])
                        # Wait for a while
                        await self.apiroutine.wait_with_timeout(5)
                        continue
                    elif m is conndown:
                        # Connection lost, no longer need to trace the port changes
                        break
        finally:
            self._portchanging.remove(conn)
