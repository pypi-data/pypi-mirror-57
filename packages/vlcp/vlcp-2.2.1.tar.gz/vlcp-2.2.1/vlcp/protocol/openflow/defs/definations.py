'''
Created on 2015/7/30

:author: hubo
'''
from . import openflow10
from . import openflow13
from . import openflow14
definations = {openflow10.OFP_VERSION: openflow10,
               openflow13.OFP_VERSION: openflow13,
               openflow14.OFP_VERSION: openflow14}
