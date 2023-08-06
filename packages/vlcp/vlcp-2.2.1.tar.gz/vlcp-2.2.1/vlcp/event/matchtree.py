'''
Created on 2015/06/01

:author: hubo
'''
from __future__ import print_function, absolute_import, division 
from collections import OrderedDict

class MatchTree(object):
    '''
    A dictionary tree for fast event match
    '''
    def __init__(self, parent = None):
        '''
        Constructor
        '''
        self.index = {}
        #self.matchers = OrderedDict()
        # JIT friendly
        self.matchers_list = []
        self.matchers_dict = None
        self._use_dict = False
        self.parent = parent
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
    
    def subtree(self, matcher, create = False):
        '''
        Find a subtree from a matcher
        
        :param matcher: the matcher to locate the subtree. If None, return the root of the tree.
        
        :param create: if True, the subtree is created if not exists; otherwise return None if not exists
        '''
        if matcher is None:
            return self
        current = self
        for i in range(self.depth, len(matcher.indices)):
            ind = matcher.indices[i]
            if ind is None:
                # match Any
                if hasattr(current, 'any'):
                    current = current.any
                else:
                    if create:
                        cany = MatchTree(current)
                        cany.parentIndex = None
                        current.any = cany
                        current = cany
                    else:
                        return None
            else:
                current2 = current.index.get(ind)
                if current2 is None:
                    if create:
                        cind = MatchTree(current)
                        cind.parentIndex = ind 
                        current.index[ind] = cind
                        current = cind
                    else:
                        return None
                else:
                    current = current2
        return current        
    def insert(self, matcher, obj):
        '''
        Insert a new matcher
        
        :param matcher: an EventMatcher
        
        :param obj: object to return
        '''
        current = self.subtree(matcher, True)
        #current.matchers[(obj, matcher)] = None
        if current._use_dict:
            current.matchers_dict[(obj, matcher)] = None
        else:
            current.matchers_list.append((obj, matcher))
        return current
    def remove(self, matcher, obj):
        '''
        Remove the matcher
        
        :param matcher: an EventMatcher
        
        :param obj: the object to remove
        '''
        current = self.subtree(matcher, False)
        if current is None:
            return
        # Assume that this pair only appears once
        if current._use_dict:
            try:
                del current.matchers_dict[(obj, matcher)]
            except KeyError:
                pass
        else:
            if len(current.matchers_list) > 10:
                # Convert to dict
                current.matchers_dict = OrderedDict((v, None) for v in current.matchers_list
                                                    if v != (obj, matcher))
                current.matchers_list = None
                current._use_dict = True
            else:
                try:
                    current.matchers_list.remove((obj, matcher))
                except ValueError:
                    pass
        while ((not current.matchers_dict) if current._use_dict
               else (not current.matchers_list))\
                and not current.matchers_dict\
                and not hasattr(current,'any')\
                and not current.index and current.parent is not None:
            # remove self from parents
            ind = current.parentIndex
            if ind is None:
                del current.parent.any
            else:
                del current.parent.index[ind]
            p = current.parent
            current.parent = None
            current = p
    def matchesWithMatchers(self, event):
        '''
        Return all matches for this event. The first matcher is also returned for each matched object.
        
        :param event: an input event
        '''
        ret = []
        self._matches(event, set(), ret)
        return tuple(ret)
    def matches(self, event):
        '''
        Return all matches for this event. The first matcher is also returned for each matched object.
        
        :param event: an input event
        '''
        ret = []
        self._matches(event, set(), ret)
        return tuple(r[0] for r in ret)
    def _matches(self, event, duptest, retlist):
        # 1. matches(self.index[ind], event)
        # 2. matches(self.any, event)
        # 3. self.matches
        if self.depth < len(event.indices):
            ind = event.indices[self.depth]
            if ind in self.index:
                self.index[ind]._matches(event, duptest, retlist)
            if hasattr(self, 'any'):
                self.any._matches(event, duptest, retlist)
        if self._use_dict:
            for v in self.matchers_dict:
                o, m = v
                if o not in duptest and m.judge(event):
                    duptest.add(o)
                    retlist.append(v)
        else:
            for v in self.matchers_list:
                o, m = v
                if o not in duptest and m.judge(event):
                    duptest.add(o)
                    retlist.append(v)
            
    def matchfirst(self, event):
        '''
        Return first match for this event
        
        :param event: an input event
        '''
        # 1. matches(self.index[ind], event)
        # 2. matches(self.any, event)
        # 3. self.matches
        if self.depth < len(event.indices):
            ind = event.indices[self.depth]
            if ind in self.index:
                m = self.index[ind].matchfirst(event)
                if m is not None:
                    return m
            if hasattr(self, 'any'):
                m = self.any.matchfirst(event)
                if m is not None:
                    return m
        if self._use_dict:
            for o, m in self.matchers_dict:
                if m is None or m.judge(event):
                    return o
        else:
            for o, m in self.matchers_list:
                if m is None or m.judge(event):
                    return o
                
    def matchfirstwithmatcher(self, event):
        '''
        Return first match with matcher for this event
        
        :param event: an input event
        '''
        # 1. matches(self.index[ind], event)
        # 2. matches(self.any, event)
        # 3. self.matches
        if self.depth < len(event.indices):
            ind = event.indices[self.depth]
            if ind in self.index:
                m = self.index[ind].matchfirstwithmatcher(event)
                if m is not None:
                    return m
            if hasattr(self, 'any'):
                m = self.any.matchfirstwithmatcher(event)
                if m is not None:
                    return m
        if self._use_dict:
            for v in self.matchers_dict:
                o, m = v
                if m is None or m.judge(event):
                    return v
        else:
            for v in self.matchers_list:
                o, m = v
                if m is None or m.judge(event):
                    return v                
        return None
    

class EventTree(object):
    '''
    Store events; match matchers
    '''
    def __init__(self, parent = None, branch = 5):
        '''
        Constructor
        '''
        self.events = []
        self.subevents = []
        self.parent = parent
        if parent is not None:
            self.depth = parent.depth + 1
        else:
            self.depth = 0
        self.branch = 5
    def subtree(self, event, create = False):
        '''
        Find a subtree from an event
        '''
        current = self
        for i in range(self.depth, len(event.indices)):
            if not hasattr(current, 'index'):
                return current
            ind = event.indices[i]
            if create:
                current = current.index.setdefault(ind, EventTree(current, self.branch))
                current.parentIndex = ind
            else:
                current = current.index.get(ind)
                if current is None:
                    return None
        return current
    def insert(self, event):
        current = self.subtree(event, True)
        if current.depth == len(event.indices):
            current.events.append(event)
        else:
            current.subevents.append(event)
            if len(current.subevents) > self.branch:
                current.index = {}
                for e in current.subevents:
                    current.insert(e)
                del current.subevents[:]
    def _returnAll(self, ret):
        ret.extend(self.events)
        if hasattr(self, 'index'):
            for st in self.index.values():
                st._returnAll(ret)
        else:
            ret.extend(self.subevents)
    def _removeFromParent(self):
        current = self
        while current.parent is not None:
            del current.parent.index[current.parentIndex]
            p = current.parent
            current.parent = None
            current = p
            if current.index or current.events:
                break
        if hasattr(current, 'index') and not current.index:
            del current.index
    def _findAndRemove(self, matcher, ret):
        current = self
        while current.depth < len(matcher.indices):
            ind = matcher.indices[current.depth]
            if not hasattr(current, 'index'):
                newsub = []
                for e in current.subevents:
                    if matcher.isMatch(e, current.depth):
                        ret.append(e)
                    else:
                        newsub.append(e)
                current.subevents = newsub
                if not current.subevents and not current.events:
                    current._removeFromParent()
                return
            elif ind is None:
                for st in current.index.values():
                    st._findAndRemove(matcher, ret)
                return
            else:
                if ind not in current.index:
                    return
                current = current.index[ind]
        current._returnAll(ret)
        current._removeFromParent()
    def findAndRemove(self, matcher):
        ret = []
        self._findAndRemove(matcher, ret)
        return tuple(ret)
    def remove(self, event):
        current = self.subtree(event)
        if current.depth == len(event.indices):
            current.events.remove(event)
        else:
            current.subevents.remove(event)

            
