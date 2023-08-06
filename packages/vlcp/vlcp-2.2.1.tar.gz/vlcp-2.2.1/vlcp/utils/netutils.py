'''
Created on 2016/7/26

:author: think
'''
from vlcp.utils.ethernet import ip4_addr

def parse_ip4_network( network ):

    ip,f,prefix = network.partition('/')
    if not f or not prefix:
        raise ValueError('invalid cidr ' + network)
    if not 0 <= int(prefix) <= 32:
        raise ValueError("invalid prefix " + prefix)

    netmask = get_netmask(prefix)

    value = ip4_addr(ip)
    return value & netmask,int(prefix)

def get_netmask(prefix):
    return (0xffffffff) >> (32 - int(prefix)) << (32 - int(prefix))

def get_network(ip, prefix):
    return ip & get_netmask(prefix)

def get_broadcast(network, prefix):
    return network | ((1 << (32 - prefix)) - 1)

def parse_ip4_address(address):
    return ip4_addr(address)

def ip_in_network(ip,network,prefix):
    shift = 32 - prefix
    return (ip >> shift) == (network >> shift)

def network_first(network,prefix):
    return network + 1

def network_last(network,prefix):
    hostmask = (1 << (32 - prefix)) - 1
    # calc cidr last avaliable ip , so inc 1
    return (network | hostmask) - 1

def format_network_cidr(cidr, strict=False):
    ip,f,prefix = cidr.partition('/')

    try:
        ip = check_ip_address(ip)
    except Exception:
        raise ValueError("Invalid CIDR " + cidr)
    if f and prefix:
        try:
            prefix = int(prefix)
            assert 0 <= prefix<= 32
        except Exception:
            raise ValueError("Invalid CIDR " + cidr)
        else:
            netmask = get_netmask(prefix)
            ip = ip & netmask
            return ip4_addr.formatter(ip) + "/" + str(prefix)
    else:
        if strict:
            raise ValueError("Invalid CIDR " + cidr)
        return ip4_addr.formatter(ip) + "/32"

def check_ip_address(ipaddress):
    try:
        ip = ip4_addr(ipaddress)
    except Exception:
        raise ValueError("Invalid IP address " + ipaddress)
    
    return ip


def format_ip_address(ipaddress):
    return ip4_addr.formatter(check_ip_address(ipaddress))

