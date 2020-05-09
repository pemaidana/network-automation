from pyats import aetest
import logging
import textfsm
from pyats.log.utils import banner


# TextFSM template for cisco_ios_show_vlan
template = open('cisco_ios_show_vlan.template')

# Compare these vlans [lists] with output from device (# show vlan br)
vlan10 = ['10', 'Vlan 10', 'active']
vlan20 = ['20', 'Vlan 20', 'active']
vlan30 = ['30', 'Vlan 30', 'active']
vlan40 = ['40', 'Vlan 40', 'active']


# get your logger for your script
logger = logging.getLogger(__name__)

class CommonSetup(aetest.CommonSetup):

    @aetest.subsection
    def check_topology(
            self,
            testbed,
            SW_CORE_1_name = 'SW_CORE_1'):

        SW_CORE_1 = testbed.devices[SW_CORE_1_name]
        
        # add them to testscript parameters
        self.parent.parameters.update(
            SW_CORE_1 = SW_CORE_1)