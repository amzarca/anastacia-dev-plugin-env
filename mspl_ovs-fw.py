# # -*- coding: utf-8 -*-
"""
This python module implements a MSPL->OVS-fw plugin inside the ANASTACIA European Project,
extending the MSPL language defined in secured project.
How to use:
    python3 mspl_ovs-fw.py [MSPL_FILE.xml]

"""
__author__ = "Abderrahmane Boudi"
__copyright__ = "Copyright 2018, ANASTACIA H2020"
__credits__ = ["Antonio Skarmeta", "Jorge Bernal Bernabé", "Alejandro Molina Zarca", "Abderrahmane Boudi"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Abderrahmane Boudi"
__email__ = "abderrahmane.boudi@aalto.fi"
__status__ = "Development"


import sys,os
import json
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Insert the parent path into the sys.path in order to import the mspl
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
import mspl


"""
    Output example:
    {"output":{in_port=1, dl_type=0x0800, nw_src=SensorA-IP, nw_dst=IoT-Broker-IP, nw_proto=6, tp_src=34567, tp_dst=80, actions=2}}
"""


class ITResourceType(mspl.ITResourceType):

    def get_configuration(self):
        """Translate the ITResource element to OVS-fw configuration"""
        capability_name = self.configuration.capability[0].Name
        if not capability_name in mspl.CapabilityType.itervalues():
            raise ValueError('The capability {} does not exist, please try with the current supported capabilities'.format(capability_name))
        # In filtering case, call translation for filtering Action and filtering conf condition
        try:
            capability_configuration_function = getattr(self, "get_{}_configuration".format(capability_name))
        except AttributeError as e:
            print("Currently, {} is not implemented.".format(capability_name))
            print(e)
            sys.exit(1)

        action, capability_enabler_conf = capability_configuration_function()
        # Build the enabler configuration, since the action is mandatory is not neccesary to check it
        enabler_conf = "{}actions={}\\n".format(capability_enabler_conf if capability_enabler_conf else "" , action)
        return enabler_conf

    def get_Filtering_L4_configuration(self):
        """Returns the configuration for Filtering_L4 capability"""
        # For filtering it is only needed the first configuration rule
        try:
            configuration_rule = self.configuration.configurationRule[0]
        except:
            print("Filtering_L4 capability requires at least a configurationRule element")
            sys.exit(1)
        action = configuration_rule.configurationRuleAction.get_configuration()
        filtering_enabler_conf = configuration_rule.configurationCondition.get_configuration()
        # Timing condition
        # TODO if neccesary
        # Application condition is not relevant on OVS-fw
        return action, filtering_enabler_conf

    def get_Forwarding_configuration(self):
        # TODO
        # Forwarding will require at least two configuration rules
        # origin = self.configuration.configurationRule[0].configurationCondition.get_configuration()
        # fwd = self.configuration.configurationRule[1].configurationCondition.get_configuration()
        pass


class FilteringAction(mspl.FilteringAction):
    def get_configuration(self):
        """Returns the filtering action for OVS-fw"""
        filtering_action = {"ALLOW": "2", "DENY": "drop"}
        return filtering_action.get(self.FilteringActionType, "drop")


class FilteringConfigurationCondition(mspl.FilteringConfigurationCondition):
    def get_configuration(self):
        """Returns the translated filtering ONOS parameters"""
        filtering_enabler_conf = ''
        packet_filter_condition = self.packetFilterCondition

        if not packet_filter_condition:
            return None

        src_addr = packet_filter_condition.SourceAddress
        dst_addr = packet_filter_condition.DestinationAddress
        ver = self.get_ip_ver(src_addr or dst_addr)

        filtering_enabler_conf += "in_port={}, ".format(packet_filter_condition.Interface) if packet_filter_condition.Interface else ''
        filtering_enabler_conf += 'dl_type=0x86DD, ' if ver == 6 else 'dl_type=0x0800, '
        filtering_enabler_conf += "nw_src={}, ".format(src_addr) if src_addr else ''
        filtering_enabler_conf += "nw_dst={}, ".format(dst_addr) if dst_addr else ''
        filtering_enabler_conf += "nw_proto={}, ".format(
            self.get_ip_proto(packet_filter_condition.ProtocolType)) if packet_filter_condition.ProtocolType else ''
        filtering_enabler_conf += "tp_src={}, ".format(
            packet_filter_condition.SourcePort) if packet_filter_condition.SourcePort else ''
        filtering_enabler_conf += "tp_dst={}, ".format(
            packet_filter_condition.DestinationPort) if packet_filter_condition.DestinationPort else ''

        return filtering_enabler_conf if filtering_enabler_conf else None

    def get_ip_ver(self, addr):
        import ipaddress
        try:
            return ipaddress.ip_address(addr).version
        except:
            return None

    def get_ip_proto(self, protocol):
        protocol = protocol.lower()
        if protocol == 'tcp':
            return 6
        if protocol == 'udp':
            return 17
        return 6


class M2LPlugin:
    """OVS-fw Medium to low plugin implementation"""

    def get_configuration(self, mspl_source):
        """Return the OVS-fw configuration from the mspl_source"""
        # Customize the pyxb generated classes with our own behavior
        global mspl
        mspl.ITResourceType._SetSupersedingClass(ITResourceType)
        mspl.FilteringAction._SetSupersedingClass(FilteringAction)
        mspl.FilteringConfigurationCondition._SetSupersedingClass(FilteringConfigurationCondition)
        # Load the xml
        it_resource = mspl.CreateFromDocument(mspl_source)
        # Start the parser process using the xml root element
        return it_resource.get_configuration()


if __name__ == "__main__":
    xml_file = sys.argv[1]
    # Instantiate the plugin
    m2lplugin = M2LPlugin()
    logger.info("Reading mspl file...")
    xml_source = open(xml_file).read()
    logger.info("Translating mspl to OVS-fw...")
    enabler_configuration = m2lplugin.get_configuration(xml_source)
    # Pretty print
    separator = "*"
    separator_group = separator*5
    title = "OVS-fw CONFIGURATION"
    print("\n{}{}{}".format(separator_group, title, separator_group))
    print(enabler_configuration)
    print("{}{}{}\n".format(separator_group, separator*len(title), separator_group))
