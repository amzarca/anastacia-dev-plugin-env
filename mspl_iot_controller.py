# # -*- coding: utf-8 -*-
"""
This python module implements a MSPL->IoTController Northbound plugin inside the ANASTACIA European Project,
extending the MSPL language defined in secured project.
How to test:
	python3 mspl_iot_controller.py test/[MSPL_FILE.xml]

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
	target=[TARGET]&method=[METHOD]&resource=[RESOURCE]&payload=[PAYLOAD]
	{
        “target”: “aaaa::2”,
        "port": "5683",
        “method”: “PUT”,
        “resource”:”.reset”
        “payload”: 1
    }
"""

class ITResourceType(mspl.ITResourceType):

	def get_configuration(self):
		'Translate the ITResource element to IoT Controller Northbound configuration'
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
		# Build the iot controller northbound parameters
		#enabler_conf = "target={}&method={}&resource={}&payload={}".format(enabler_configuration["target"], enabler_configuration["method"], enabler_configuration["resource"], enabler_configuration["payload"])
		return json.dumps(enabler_configuration)


	def get_IoT_control_configuration(self):
		'Returns the configuration for IoT Control capability'
		try:
			configuration_rule = self.configuration.configurationRule[0]
		except:
			print("IoT_control capability requires at least a configurationRule element")
			sys.exit(1)
		payload = configuration_rule.configurationRuleAction.get_configuration()
		target,port,resource,method = configuration_rule.configurationCondition.get_configuration()

		enabler_configuration = {'target':target,'port':port,'method':method,'resource':resource,'payload':payload}

		return enabler_configuration


class PowerMgmtAction(mspl.PowerMgmtAction):
	def get_configuration(self):
		'Returns the power management action for IoT Controller'
		POWER_MANAGEMENT_ACTIONS = {"OFF": "1"}
		return POWER_MANAGEMENT_ACTIONS.get(self.PowerMgmtActionType,"1")

class BootstrappingAction(mspl.BootstrappingAction):
	def get_configuration(self):
		'Returns the payload for Bottstrapping action for IoT Controller'
		return 1

class FilteringConfigurationCondition(mspl.FilteringConfigurationCondition):
	def get_configuration(self):
		'Returns the IoT device address or ID'
		packet_filter_condition = self.packetFilterCondition
		if not packet_filter_condition:
			return None

		target = packet_filter_condition.DestinationAddress if packet_filter_condition.DestinationAddress else ""
		port = packet_filter_condition.DestinationPort if packet_filter_condition.DestinationPort else ""

		iot_application_layer_condition = self.applicationLayerCondition
		if not iot_application_layer_condition:
			return None	

		resource,method = iot_application_layer_condition.get_configuration()

		return target,port,resource,method


class IoTApplicationLayerCondition(mspl.IoTApplicationLayerCondition):
	def get_configuration(self):
		'Returns the IoT resource and method'

		resource = self.URL if self.URL else ""
		method = self.method if self.method else ""

		return resource,method


class M2LPlugin:
	'IoT Controller Medium to low plugin implementation'

	def get_configuration(self,mspl_source):
		'Return the IoT Controller configuration from the mspl_source'
		# Customize the pyxb generated classes with our own behavior
		global mspl
		mspl.ITResourceType._SetSupersedingClass(ITResourceType)
		mspl.PowerMgmtAction._SetSupersedingClass(PowerMgmtAction)
		mspl.BootstrappingAction._SetSupersedingClass(BootstrappingAction)
		mspl.FilteringConfigurationCondition._SetSupersedingClass(FilteringConfigurationCondition)
		mspl.IoTApplicationLayerCondition._SetSupersedingClass(IoTApplicationLayerCondition)
		#Load the xml
		it_resource = mspl.CreateFromDocument(mspl_source)
		# Start the parser process using the xml root element
		return it_resource.get_configuration()

if __name__ == "__main__":
	xml_file = sys.argv[1] 
	m2lplugin = M2LPlugin()
	logger.info("Reading mspl file...")
	xml_source = open(xml_file).read()
	enabler_configuration = m2lplugin.get_configuration(xml_source)
	# Pretty print
	separator = "*"
	separator_group = separator*5
	title = "{} CONFIGURATION".format(sys.argv[0].split("mspl_")[1][:-3].upper())
	print("\n{}{}{}".format(separator_group,title,separator_group))
	print(enabler_configuration)
	print("{}{}{}\n".format(separator_group,separator*len(title),separator_group))