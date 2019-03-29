# # -*- coding: utf-8 -*-
"""
This python module implements a MSPL->IPTABLES plugin inside the ANASTACIA European Project,
extending the MSPL language defined in secured project.
How to use:
	python3 mspl_iptables.py [MSPL_FILE.xml]

"""
__author__ = "Alejandro Molina Zarca"
__copyright__ = "Copyright 2018, ANASTACIA H2020"
__credits__ = ["Antonio Skarmeta", "Jorge Bernal Bernabé", "Alejandro Molina Zarca"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Alejandro Molina Zarca"
__email__ = "alejandro.mzarca@um.es"
__status__ = "Development"


import sys,os
import json
# Insert the parent path into the sys.path in order to import the mspl
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import mspl

"""
	Filtering Output example:
	{"output":{"psa_config":"*filter\n:INPUT ACCEPT [0:0]\n:OUTPUT ACCEPT [0:0]\n:FORWARD ACCEPT [0:0]\n-A FORWARD -p TCP -m time --timestart 08:00 --timestop 19:00 -j DROP\n-A FORWARD -p UDP -m time --timestart 08:00 --timestop 19:00 -j DROP\nCOMMIT\n"}}
	
	Forwarding Example
	TODO

	Iptables Examples:
	https://www.cert.org/downloads/IPv6/ip6tables_rules.txt
	http://net.doit.wisc.edu/~dwcarder/captivator/linux_l2_firewalling.txt
	https://www.debuntu.org/how-to-redirecting-network-traffic-to-a-new-ip-using-iptables/
"""

class ITResourceType(mspl.ITResourceType):

	def get_configuration(self):
		'Translate the ITResource element to IPTABLES configuration'
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
		enabler_conf = "FORWARD{} -j {}".format(capability_enabler_conf if capability_enabler_conf else "" , action)
		return enabler_conf

	def get_Filtering_L4_configuration(self):
		'Returns the configuration for Filtering_L4 capability'
		# For filtering it is only needed the first configuration rule
		try:
			configuration_rule = self.configuration.configurationRule[0]
		except:
			print("Filtering_L4 capability requires at least a configurationRule element")
			sys.exit(1)
		action = configuration_rule.configurationRuleAction.get_configuration()
		filtering_enabler_conf = configuration_rule.configurationCondition.get_configuration()
		#Timing condition
		# TODO if neccesary
		#Application condition is not relevant on iptables
		return (action,filtering_enabler_conf)

	def get_Forwarding_configuration(self):
		#TODO
		# Forwarding will require at least two configuration rules
		#origin = self.configuration.configurationRule[0].configurationCondition.get_configuration()
		#fwd = self.configuration.configurationRule[1].configurationCondition.get_configuration()
		pass

class FilteringAction(mspl.FilteringAction):
	def get_configuration(self):
		'Returns the filtering action for IPTABLES'
		FILTERING_ACTION = {"ALLOW": "ACCEPT", "DENY":"DROP"}
		return FILTERING_ACTION.get(self.FilteringActionType,"DROP")

class FilteringConfigurationCondition(mspl.FilteringConfigurationCondition):
	def get_configuration(self):
		'Returns the traslated filtering IPTABLES parameters'
		filtering_enabler_conf = ""
		packet_filter_condition = self.packetFilterCondition
		if not packet_filter_condition:
			return None
		filtering_enabler_conf+=" -s {}".format(packet_filter_condition.SourceAddress) if packet_filter_condition.SourceAddress else ""
		filtering_enabler_conf+=" -d {}".format(packet_filter_condition.DestinationAddress) if packet_filter_condition.DestinationAddress else ""
		filtering_enabler_conf+=" -p {}".format(packet_filter_condition.ProtocolType) if packet_filter_condition.ProtocolType else ""
		filtering_enabler_conf+=" --source-port {}".format(packet_filter_condition.SourcePort) if packet_filter_condition.SourcePort else ""
		filtering_enabler_conf+=" -m state --state {}".format(",".join(packet_filter_condition.State)) if packet_filter_condition.State else ""
		filtering_enabler_conf+=" --destination-port {}".format(packet_filter_condition.DestinationPort) if packet_filter_condition.DestinationPort else ""
		filtering_enabler_conf+=" -i {}".format(packet_filter_condition.Interface) if packet_filter_condition.Interface else ""
		return filtering_enabler_conf if filtering_enabler_conf else None

class M2LPlugin:
	'IPTABLES Medium to low plugin implementation'

	def get_configuration(self,mspl_source):
		'Return the IPTABLES configuration from the mspl_source'
		# Customize the pyxb generated classes with our own behavior
		global mspl
		mspl.ITResourceType._SetSupersedingClass(ITResourceType)
		mspl.FilteringAction._SetSupersedingClass(FilteringAction)
		mspl.FilteringConfigurationCondition._SetSupersedingClass(FilteringConfigurationCondition)
		#Load the xml
		logger.info("IPTABLES plugin started for".format(mspl_source))
		it_resource = mspl.CreateFromDocument(mspl_source)
		# Start the parser process using the xml root element
		return it_resource.get_configuration()

if __name__ == "__main__":
	xml_file = sys.argv[1] 
	m2lplugin = M2LPlugin()
	print("Reading mspl file...")
	xml_source = open(xml_file).read()
	enabler_configuration = m2lplugin.get_configuration(xml_source)
	# Pretty print
	separator = "*"
	separator_group = separator*5
	title = "{} CONFIGURATION".format(sys.argv[0].split("mspl_")[1][:-3].upper())
	print("\n{}{}{}".format(separator_group,title,separator_group))
	print(enabler_configuration)
	print("{}{}{}\n".format(separator_group,separator*len(title),separator_group))