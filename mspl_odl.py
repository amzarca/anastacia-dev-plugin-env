# # -*- coding: utf-8 -*-
"""
This python module implements a MSPL->OpenDayLight plugin inside the ANASTACIA European Project,
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

	<?xml version="1.0" encoding="UTF-8" standalone="no"?>
	<flow xmlns="urn:opendaylight:flow:inventory">
		<priority>[PRIORITY]</priority>
		<flow-name>[FLOW-NAME]</flow-name>
		<match>
			<ethernet-match>
				<ethernet-source>
					<address>[ADDR]</address>
				</ethernet-source>
			</ethernet-match>
		</match>
		<id>Dropper</id>
		<table_id>0</table_id>
		<instructions>
			<instruction>
				<order>0</order>
				<apply-actions>
					<action>
					   <order>0</order>
					   <drop-action/>
					</action>
				</apply-actions>
			</instruction>
		</instructions>
	</flow>
	Forwarding Example
	TODO

	OpenDayLight Examples:
	https://wiki.opendaylight.org/view/OpenDaylight_OpenFlow_Plugin:End_to_End_Flows
	https://wiki.opendaylight.org/view/Editing_OpenDaylight_OpenFlow_Plugin:End_to_End_Flows:Example_Flows
"""

class ITResourceType(mspl.ITResourceType):


	def fill_restconf_template(self,enabler_configuration):
		
		result = '''
			{{
				"id": "{name}",
				"priority": {priority},
				"table_id": 0,
				"flow-name": "{name}",
				"instructions": {{
					"instruction": [
						{{
							"order": 0,
							"apply-actions": {{
								"action": [
									{{
									  "order": 0,
									  {action}
									}}
								  ]
							}}
						}}
					]
				}},
				"match": {{
					"ethernet-match": {{
						"ethernet-type": {{
							"type": "34525"
						}}
					}},
					{filtering_enabler_conf}
				}}
			}}
		'''.format(priority=enabler_configuration["priority"],name=enabler_configuration["name"],filtering_enabler_conf=enabler_configuration["filtering_enabler_conf"],\
				action=enabler_configuration["action"])
		logger.info(result)
		return json.loads(result)
		





		"""
		return '''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
		<flow xmlns="urn:opendaylight:flow:inventory">
			<priority>{}</priority>
			<flow-name>{}</flow-name>
			<match>
				{}
			</match>
			<id>{}</id>
			<table_id>0</table_id>
			<instructions>
				<instruction>
					<order>0</order>
					<apply-actions>
						<action>
							<order>0</order>
							{}
						</action>
					</apply-actions>
				</instruction>
			</instructions>
		</flow>
		'''.format(enabler_configuration["priority"],enabler_configuration["name"],enabler_configuration["filtering_enabler_conf"],\
				enabler_configuration["name"],enabler_configuration["action"])
		"""


	def get_configuration(self):
		'Translate the ITResource element to OpenDayLight configuration'
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

		return enabler_configuration

	def get_Forwarding_configuration(self):
		#TODO
		pass

class FilteringAction(mspl.FilteringAction):
	def get_configuration(self):
		'Returns the filtering action for OpenDayLight'
		#FILTERING_ACTION = {"ALLOW": "<output-node-connector>CONTROLLER</output-node-connector>", "DENY":"<drop-action/>"}
		FILTERING_ACTION = {"ALLOW": '"output-node-connector":"CONTROLLER"', "DENY":'"drop-action": {}'}
		return FILTERING_ACTION.get(self.FilteringActionType,"DENY")



class Priority(mspl.Priority):
	def get_configuration(self):
		'Returns the priority of the configuration rule'
		return self.value_ if self.value_ else 0

class FilteringConfigurationCondition(mspl.FilteringConfigurationCondition):
	def get_configuration(self):
		'Returns the traslated filtering OpenDayLight parameters'
		filtering_enabler_conf = []
		packet_filter_condition = self.packetFilterCondition
		if not packet_filter_condition:
			return None

		filtering_enabler_conf.append('"ipv6-source":"{}"'.format(packet_filter_condition.SourceAddress)) if packet_filter_condition.SourceAddress else ""
		filtering_enabler_conf.append('"ipv6-destination":"{}"'.format(packet_filter_condition.DestinationAddress)) if packet_filter_condition.DestinationAddress else ""
		protocol=packet_filter_condition.ProtocolType if packet_filter_condition.ProtocolType else ""
		if protocol:
			if "icmp" in protocol.lower():
				filtering_enabler_conf.append('''
				"icmpv6-match":{
					"icmpv6-type":6,
					"icmpv6-code":0
				}''')
			else:
				filtering_enabler_conf.append('"{}-source-port":{}'.format(protocol,packet_filter_condition.SourcePort,protocol)) if packet_filter_condition.SourcePort else ""
				filtering_enabler_conf.append('"{}-destination-port":{}'.format(protocol,packet_filter_condition.DestinationPort,protocol)) if packet_filter_condition.DestinationPort else ""
		filtering_enabler_conf.append('"in-port":{}'.format(packet_filter_condition.Interface)) if packet_filter_condition.Interface else ""
		logger.info(",\n".join(filtering_enabler_conf))
		return ",\n".join(filtering_enabler_conf) if filtering_enabler_conf else None


		"""
		filtering_enabler_conf+="<ipv6-source>{}</ipv6-source>".format(packet_filter_condition.SourceAddress) if packet_filter_condition.SourceAddress else ""
		filtering_enabler_conf+="<ipv6-destination>{}</ipv6-destination>".format(packet_filter_condition.DestinationAddress) if packet_filter_condition.DestinationAddress else ""
		protocol=packet_filter_condition.ProtocolType if packet_filter_condition.ProtocolType else ""
		if protocol:
			if "icmp" in protocol.lower():
				filtering_enabler_conf+='''
				<icmpv6-match>
					<icmpv6-type>6</icmpv6-type>
					<icmpv6-code>6</icmpv6-code>
				</icmpv6-match>'''
			else:
				filtering_enabler_conf+="<{}-source-port>{}</{}-source-port>".format(protocol,packet_filter_condition.SourcePort,protocol) if packet_filter_condition.SourcePort else ""
				filtering_enabler_conf+="<{}-destination-port>{}</{}-destination-port>".format(protocol,packet_filter_condition.DestinationPort,protocol) if packet_filter_condition.DestinationPort else ""
		filtering_enabler_conf+="<in-port>{}</in-port>".format(packet_filter_condition.Interface) if packet_filter_condition.Interface else ""
		return filtering_enabler_conf if filtering_enabler_conf else None
		"""
class M2LPlugin:
	'OpenDayLight Medium to low plugin implementation'

	def get_configuration(self,mspl_source):
		'Return the OpenDayLight configuration from the mspl_source'
		# Customize the pyxb generated classes with our own behavior
		global mspl
		mspl.ITResourceType._SetSupersedingClass(ITResourceType)
		mspl.FilteringAction._SetSupersedingClass(FilteringAction)
		mspl.Priority._SetSupersedingClass(Priority)
		mspl.FilteringConfigurationCondition._SetSupersedingClass(FilteringConfigurationCondition)
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