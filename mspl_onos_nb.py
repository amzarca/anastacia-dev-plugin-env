# # -*- coding: utf-8 -*-
"""
This python module implements a MSPL->ONOS Northbound API plugin inside the ANASTACIA European Project,
extending the MSPL language defined in secured project.
How to use:
	python3 mspl_odl.py [MSPL_FILE.xml]

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

	{
	  "priority": 60000,
	  "timeout": 0,
	  "isPermanent": true,
	  "deviceId": "of:000008002768a30a",
	  "treatment": {
	    "instructions": [
	      {
	        "type": "NOACTION"
	      }
	    ]
	  },
	  "selector": {
	    "criteria": [
	      {
	        "type": "ETH_TYPE",
	        "ethType": "0x86dd"
	      },
	      {
	        "type": "IPV6_SRC",
	        "ip": "aaaa::212:7402:2:202/64"
	      }
	    ]
	  }
	}

	Forwarding Example
	TODO

	ONOS NB API:
	https://wiki.onosproject.org/display/ONOS/Flow+Rules
	http://[CNTROLLER_IP]:8181/onos/v1/docs/#!/docs/get_docs_index_html

"""

class ITResourceType(mspl.ITResourceType):


	def fill_restconf_template(self,enabler_configuration):
		
		# loads and dumps in order to armonize the tabs
		return json.dumps(json.loads('''
  			{{
				"priority": {},
				"tableId": 0,
				"timeout": 0,
				"isPermanent": true,
				"deviceId": "[DEVICE_ID (e.g. of:000008002768a30a)]",
				"treatment": {{
				    "instructions": [
				      	{}
				    ]
				}},
				"selector": {{
				    "criteria": [
				      {{
				        "type": "ETH_TYPE",
				        "ethType": "0x86dd"
				      }},
				      	{}
				    ]
				}}
			}}
			'''.format(enabler_configuration["priority"],enabler_configuration["action"],enabler_configuration["filtering_enabler_conf"])),indent=4)

	def get_configuration(self):
		'Translate the ITResource element to ONOS Northbound API configuration'
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

		enabler_configuration = capability_configuration_function()
		# Build the enabler configuration, since the action is mandatory is not neccesary to check it
		enabler_conf = self.fill_restconf_template(enabler_configuration)
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
		name = configuration_rule.Name
		priority = configuration_rule.externalData.get_configuration()

		enabler_configuration = {'action':action,'filtering_enabler_conf':filtering_enabler_conf,'name':name,'priority':priority}


		print("enabler_configuration:",enabler_configuration)

		return enabler_configuration

	def get_Traffic_Divert_configuration(self):
		# For Traffic Divert it is only needed the first configuration rule
		try:
			configuration_rule = self.configuration.configurationRule[0]
		except:
			print("Traffic Divert capability requires at least a configurationRule element")
			sys.exit(1)
		# Get the action for Traffic divert
		action = configuration_rule.configurationRuleAction.get_configuration()
		# Get the criteria
		traffic_divert_enabler_conf = configuration_rule.configurationCondition.get_configuration()
		name = configuration_rule.Name
		priority = configuration_rule.externalData.get_configuration()


		enabler_configuration = {'action':action,'filtering_enabler_conf':traffic_divert_enabler_conf,'name':name,'priority':priority}

		print("enabler_configuration:",enabler_configuration)
		
		return enabler_configuration

class FilteringAction(mspl.FilteringAction):
	def get_configuration(self):
		'Returns the filtering action for ONOS Northbound API'
		ALLOW = "ALLOW"
		DENY = "DENY"
		no_action_type = {"type": "NOACTION"}
		fwd = {"type": "OUTPUT",
        			"port": "CONTROLLER"}
		FILTERING_ACTION = {"ALLOW": fwd, "DENY":no_action_type}
		       	
		if self.FilteringActionType.isdigit():
			action_type = FILTERING_ACTION.get(ALLOW)
			action_type["port"] = self.FilteringActionType
			logger.info(json.dumps(action_type))
			return json.dumps(action_type)
		
		return json.dumps(FILTERING_ACTION.get(self.FilteringActionType,DENY))

class Priority(mspl.Priority):
	def get_configuration(self):
		'Returns the priority of the configuration rule'
		return self.value_ if self.value_ else 0


class FilteringConfigurationCondition(mspl.FilteringConfigurationCondition):
	def get_configuration(self):
		'Returns the traslated filtering ONOS Northbound API parameters'
		filtering_enabler_conf = []
		packet_filter_condition = self.packetFilterCondition
		if not packet_filter_condition:
			return None

		#TODO: Verify ipv4 or ipv6
		ip_version = "6"
		filtering_enabler_conf.append({"type":"IPV{}_SRC".format(ip_version),"ip":packet_filter_condition.SourceAddress})  if packet_filter_condition.SourceAddress else ""
		filtering_enabler_conf.append({"type":"IPV{}_DST".format(ip_version),"ip":packet_filter_condition.DestinationAddress}) if packet_filter_condition.DestinationAddress else ""
		protocol=packet_filter_condition.ProtocolType if packet_filter_condition.ProtocolType else ""
		if protocol:
			# IANA proto id: https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml
			PROTOCOL_ID = {"ICMP":58,"TCP":6,"UDP":17,"IPV6":41}

			filtering_enabler_conf.append({"type":"IP_PROTO","protocol":PROTOCOL_ID[protocol.upper()]})

			#if "ICMP" in protocol.upper():
				#https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml#icmpv6-parameters-2
			#	filtering_enabler_conf.append({"type":"ICMPV{}_TYPE".format(ip_version),"icmpv{}Type".format(ip_version):1})
			#	filtering_enabler_conf.append({"type":"ICMPV{}_CODE".format(ip_version),"icmpv{}Code".format(ip_version):1})
			#else:
			filtering_enabler_conf.append({"type":"{}_SRC".format(protocol),"{}Port".format(protocol.lower()):packet_filter_condition.SourcePort}) if packet_filter_condition.SourcePort else ""
			filtering_enabler_conf.append({"type":"{}_DST".format(protocol),"{}Port".format(protocol.lower()):packet_filter_condition.DestinationPort})  if packet_filter_condition.DestinationPort else ""
		filtering_enabler_conf.append({"type":"IN_PORT","port":packet_filter_condition.Interface})  if packet_filter_condition.Interface else ""
		return json.dumps(filtering_enabler_conf)[1:-1] if filtering_enabler_conf else None


class TrafficDivertConfigurationCondition(mspl.TrafficDivertConfigurationCondition):
	def get_configuration(self):
		# We cannot use super because the inheritance implementation of pyxb
		return FilteringConfigurationCondition.get_configuration(self)

class TrafficDivertAction(mspl.TrafficDivertAction):
	def get_configuration(self):
		'Returns the filtering action for ONOS Northbound API'
		FORWARD = "FORWARD"
		# Get the destination
		destination = self.packetDivertAction.packetFilterCondition.Interface if self.packetDivertAction.packetFilterCondition.Interface else self.packetDivertAction.packetFilterCondition.DestinationAddress
		#destination = self.packetDivertAction.packetFilterCondition.DestinationAddress
		fwd = {"type": "OUTPUT",
        			"port": destination}
		TRAFFIC_DIVERT_ACTION = {"FORWARD": fwd}
		
		return json.dumps(TRAFFIC_DIVERT_ACTION.get(self.TrafficDivertActionType,FORWARD))



class M2LPlugin:
	'ONOS Northbound API Medium to low plugin implementation'

	def get_configuration(self,mspl_source):
		'Return the ONOS Northbound API configuration from the mspl_source'
		# Customize the pyxb generated classes with our own behavior
		global mspl
		mspl.ITResourceType._SetSupersedingClass(ITResourceType)
		mspl.FilteringAction._SetSupersedingClass(FilteringAction)
		mspl.Priority._SetSupersedingClass(Priority)
		mspl.FilteringConfigurationCondition._SetSupersedingClass(FilteringConfigurationCondition)
		# Traffic divert
		mspl.TrafficDivertAction._SetSupersedingClass(TrafficDivertAction)
		mspl.TrafficDivertConfigurationCondition._SetSupersedingClass(TrafficDivertConfigurationCondition)
		#Load the xml
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