# # -*- coding: utf-8 -*-
"""
This python module implements a MSPL->Cooja CSC model plugin inside the ANASTACIA European Project,
extending the MSPL language defined in secured project.

It requires the simconf files (simconf folder) to perform the translation.

How to use:
	python3 mspl_cooja.py [MSPL_FILE.xml]

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
# Insert the grandparent path into the sys.path in order to import the mspl
parentPath = os.path.abspath("..")
if parentPath not in sys.path:
    sys.path.insert(0, parentPath)
import mspl

"""
Output example:
{'method':'PUT', 'CSC':'
<?xml version="1.0" encoding="utf-8"?>
<simconf>
	<project EXPORT="discard">[APPS_DIR]/mrm</project>
	<project EXPORT="discard">[APPS_DIR]/mspsim</project>
	<project EXPORT="discard">[APPS_DIR]/avrora</project>
	<project EXPORT="discard">[APPS_DIR]/serial_socket</project>
	<project EXPORT="discard">[APPS_DIR]/collect-view</project>
	<project EXPORT="discard">[APPS_DIR]/powertracker</project>
	<simulation>
		<title>REST with RPL router</title>
		<randomseed>123456</randomseed>
		<motedelay_us>1000000</motedelay_us>
		<radiomedium>
      		org.contikios.cooja.radiomediums.UDGM
			<transmitting_range>15.0</transmitting_range>
			<interference_range>15.0</interference_range>
			<success_ratio_tx>1.0</success_ratio_tx>
			<success_ratio_rx>1.0</success_ratio_rx>
		</radiomedium>
		<events>
			<logoutput>40000</logoutput>
		</events>
		<motetype>
      		org.contikios.cooja.mspmote.WismoteMoteType
			<identifier>rplroot</identifier>
			<description>Wismote RPL Root</description>
			<source EXPORT="discard">[CONTIKI_DIR]/examples/ipv6/rpl-border-router/border-router.c</source>
			<commands EXPORT="discard">make border-router.wismote TARGET=wismote</commands>
			<firmware EXPORT="copy">[CONTIKI_DIR]/examples/ipv6/rpl-border-router/border-router.wismote</firmware>
			<moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.RimeAddress</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.IPAddress</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.Mote2MoteRelations</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.MoteAttributes</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspClock</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspMoteID</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspButton</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspDefaultSerial</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspLED</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
		</motetype>
		<motetype>
      		org.contikios.cooja.mspmote.WismoteMoteType
			<identifier>server</identifier>
			<description>Erbium Server</description>
			<source EXPORT="discard">[CONTIKI_DIR]/examples/er-rest-example/er-example-server.c</source>
			<commands EXPORT="discard">make er-example-server.wismote TARGET=wismote</commands>
			<firmware EXPORT="copy">[CONTIKI_DIR]/examples/er-rest-example/er-example-server.wismote</firmware>
			<moteinterface>org.contikios.cooja.interfaces.Position</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.RimeAddress</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.IPAddress</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.Mote2MoteRelations</moteinterface>
			<moteinterface>org.contikios.cooja.interfaces.MoteAttributes</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspClock</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspMoteID</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspButton</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.Msp802154Radio</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspDefaultSerial</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspLED</moteinterface>
			<moteinterface>org.contikios.cooja.mspmote.interfaces.MspDebugOutput</moteinterface>
		</motetype>
		<mote>
			<breakpoints></breakpoints>
			<interface_config>
        		org.contikios.cooja.interfaces.Position
				<x>0.0</x>
				<y>0.0</y>
				<z>0.0</z>
			</interface_config>
			<interface_config>
        		org.contikios.cooja.mspmote.interfaces.MspClock
				<deviation>1.0</deviation>
			</interface_config>
			<interface_config>
        		org.contikios.cooja.mspmote.interfaces.MspMoteID
				<id>1</id>
			</interface_config>
			<motetype_identifier>rplroot</motetype_identifier>
		</mote>
		<mote>
			<breakpoints></breakpoints>
			<interface_config>
        		org.contikios.cooja.interfaces.Position
				<x>10.0</x>
				<y>0.0</y>
				<z>0.0</z>
			</interface_config>
			<interface_config>
        		org.contikios.cooja.mspmote.interfaces.MspClock
				<deviation>1.0</deviation>
			</interface_config>
			<interface_config>
        		org.contikios.cooja.mspmote.interfaces.MspMoteID
				<id>2</id>
			</interface_config>
			<motetype_identifier>server</motetype_identifier>
		</mote>
		<mote>
			<breakpoints></breakpoints>
			<interface_config>
				se.sics.cooja.interfaces.Position
				<x>0.0</x>
				<y>0.0</y>
				<z>0.0</z>
			</interface_config>
			<interface_config>
				se.sics.cooja.mspmote.interfaces.MspMoteID
				<id>1</id>
			</interface_config>
			<motetype_identifier>1</motetype_identifier>
		</mote>
		</simulation>
	<plugin>
    	org.contikios.cooja.plugins.SimControl
		<width>280</width>
		<z>1</z>
		<height>160</height>
		<location_x>400</location_x>
		<location_y>0</location_y>
	</plugin>
	<plugin>
    	org.contikios.cooja.plugins.Visualizer
		<plugin_config>
			<moterelations>true</moterelations>
			<skin>org.contikios.cooja.plugins.skins.IDVisualizerSkin</skin>
			<skin>org.contikios.cooja.plugins.skins.GridVisualizerSkin</skin>
			<skin>org.contikios.cooja.plugins.skins.TrafficVisualizerSkin</skin>
			<skin>org.contikios.cooja.plugins.skins.UDGMVisualizerSkin</skin>
			<viewport>7.266366960762773 0.0 0.0 7.266366960762773 72.91888287187065 -365.1374754637069</viewport>
		</plugin_config>
		<width>400</width>
		<z>2</z>
		<height>400</height>
		<location_x>1</location_x>
		<location_y>1</location_y>
	</plugin>
	<plugin>
    	org.contikios.cooja.plugins.LogListener
		<plugin_config>
			<filter></filter>
			<formatted_time></formatted_time>
			<coloring></coloring>
		</plugin_config>
		<width>1320</width>
		<z>6</z>
		<height>240</height>
		<location_x>400</location_x>
		<location_y>160</location_y>
	</plugin>
	<plugin>
    	org.contikios.cooja.plugins.TimeLine
		<plugin_config>
			<mote>0</mote>
			<mote>1</mote>
			<showRadioRXTX></showRadioRXTX>
			<showRadioHW></showRadioHW>
			<showLEDs></showLEDs>
			<zoomfactor>500.0</zoomfactor>
		</plugin_config>
		<width>1720</width>
		<z>5</z>
		<height>166</height>
		<location_x>0</location_x>
		<location_y>709</location_y>
	</plugin>
	<plugin>
    	org.contikios.cooja.plugins.Notes
		<plugin_config>
			<notes>Enter notes here</notes>
			<decorations>true</decorations>
		</plugin_config>
		<width>1040</width>
		<z>4</z>
		<height>160</height>
		<location_x>680</location_x>
		<location_y>0</location_y>
	</plugin>
	<plugin>
    	org.contikios.cooja.serialsocket.SerialSocketServer
		<mote_arg>0</mote_arg>
		<plugin_config>
			<port>60001</port>
			<bound>true</bound>
		</plugin_config>
		<width>362</width>
		<z>3</z>
		<height>116</height>
		<location_x>20</location_x>
		<location_y>427</location_y>
	</plugin>
	<plugin>
    	org.contikios.cooja.plugins.ScriptRunner
		<plugin_config>
			<script>TIMEOUT(86400000);
		         log.log(&quot;first simulation message at time : &quot; + time + &quot;\n&quot;);
		         while (true) {
		           log.log(id + &quot; &quot; + time + &quot; &quot; + msg + &quot;\n&quot;);
		           YIELD(); /* wait for another mote output */
		         }
			</script>
			<active>true</active>
		</plugin_config>
		<width>600</width>
		<z>0</z>
		<height>700</height>
		<location_x>1094</location_x>
		<location_y>104</location_y>
	</plugin>
</simconf>'}


	Cooja examples:
	http://www.contiki-os.org/start.html

"""

class ITResourceType(mspl.ITResourceType):

	def get_configuration(self):
		'Translate the ITResource element to IoT Honeynet deployment Agent'
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
		#return enabler_configuration['CSC']
		return json.dumps(enabler_configuration)


	def get_IoT_honeynet_configuration(self):
		'Returns the configuration for IoT Control capability'
		try:
			configuration_rule = self.configuration.configurationRule[0]
		except:
			print("IoT_control capability requires at least a configurationRule element")
			sys.exit(1)

		action, csc = configuration_rule.configurationRuleAction.get_configuration()

		enabler_configuration = {'action':action,'CSC':csc}

		return enabler_configuration


class VIoTHoneyNetAction(mspl.VIoTHoneyNetAction):
	def get_configuration(self):
		'Returns the VIoTHoneynet Action action for IoT Controller'
		IOT_HONEYNET_ACTIONS = {"DEPLOY": "PUT",
									"REMOVE": "DELETE"}
		# Translates the IoT HoneyNet model to Cooja CSC
		vIoTHoneyNetConf = self.ioTHoneyNet.get_configuration()
		# The vIoTHoneyNet Agent will receive an action and the CSC configuration
		return IOT_HONEYNET_ACTIONS.get(self.VIoTHoneyNetActionType,"DELETE"), vIoTHoneyNetConf.toxml("utf-8",element_name="simconf").decode("utf-8")
		#return IOT_HONEYNET_ACTIONS.get(self.VIoTHoneyNetActionType,"DELETE"), vIoTHoneyNetConf.toDOM(element_name="simconf").toprettyxml(encoding="utf-8").decode("utf-8")

# Default iot_device configuration per model	
IoTDEVICE_MODEL = {"Sky": {"ioTRouterType":{
							"source":"[CONTIKI_DIR]/examples/ipv6/rpl-border-router/border-router.c",
							"commands":"make border-router.sky TARGET=sky",
							"firmware":"[CONTIKI_DIR]/examples/ipv6/rpl-border-router/border-router.sky"},
						"ioTHoneyPotType":{
							"source":"[CONTIKI_DIR]/examples/er-rest-example/er-example-server.c",
							"commands":"make er-example-server.sky TARGET=sky",
							"firmware":"[CONTIKI_DIR]/examples/er-rest-example/er-example-server.sky"},
						"mote_interfaces":[
							"se.sics.cooja.interfaces.Position",
							"se.sics.cooja.interfaces.RimeAddress",
							"se.sics.cooja.interfaces.IPAddress",
							"se.sics.cooja.interfaces.Mote2MoteRelations",
							"se.sics.cooja.interfaces.MoteAttributes",
							"se.sics.cooja.mspmote.interfaces.MspClock",
							"se.sics.cooja.mspmote.interfaces.MspMoteID",
							"se.sics.cooja.mspmote.interfaces.SkyButton",
							"se.sics.cooja.mspmote.interfaces.SkyFlash",
							"se.sics.cooja.mspmote.interfaces.SkyCoffeeFilesystem",
							"se.sics.cooja.mspmote.interfaces.Msp802154Radio", 
							"se.sics.cooja.mspmote.interfaces.MspSerial",
							"se.sics.cooja.mspmote.interfaces.SkyLED",
							"se.sics.cooja.mspmote.interfaces.MspDebugOutput",
							"se.sics.cooja.mspmote.interfaces.SkyTemperature"]},
					"Wismote": {"ioTRouterType":{
							"source":"[CONTIKI_DIR]/examples/ipv6/rpl-border-router/border-router.c",
							"commands":"make border-router.wismote TARGET=wismote",
							"firmware":"[CONTIKI_DIR]/examples/ipv6/rpl-border-router/border-router.wismote"},
						"ioTHoneyPotType":{
							"source":"[CONTIKI_DIR]/examples/er-rest-example/er-example-server.c",
							"commands":"make er-example-server.wismote TARGET=wismote",
							"firmware":"[CONTIKI_DIR]/examples/er-rest-example/er-example-server.wismote"},
						"mote_interfaces":[
							"org.contikios.cooja.interfaces.Position",
							"org.contikios.cooja.interfaces.RimeAddress",
							"se.sics.cooja.interfaces.IPAddress",
							"org.contikios.cooja.interfaces.Mote2MoteRelations",
							"org.contikios.cooja.interfaces.MoteAttributes",
							"org.contikios.cooja.mspmote.interfaces.MspClock",
							"org.contikios.cooja.mspmote.interfaces.MspMoteID",
							"org.contikios.cooja.mspmote.interfaces.MspButton",
							"org.contikios.cooja.mspmote.interfaces.Msp802154Radio",
							"org.contikios.cooja.mspmote.interfaces.MspDefaultSerial",
							"org.contikios.cooja.mspmote.interfaces.MspLED", 
							"org.contikios.cooja.mspmote.interfaces.MspDebugOutput"]},

				}


def generate_mote_type(**kwargs):
	'Generates a mote type according to parameters'
	from simconf import simconf

	motetype = simconf.motetypeType()

	import pyxb
	motetype.orderedContent().append(pyxb.binding.basis.NonElementContent("se.sics.cooja.mspmote.WismoteMoteType"))

	motetype.identifier = kwargs['identifier']
	motetype.description = kwargs['description']
	motetype.source = kwargs['source']
	motetype.commands = kwargs['commands']
	motetype.firmware = kwargs['firmware']

	mote_interfaces = kwargs['mote_interfaces']

	for mote_interface in mote_interfaces:
		motetype.moteinterface.append(mote_interface)

	return motetype

def generate_mote(**kwargs):
	'Instantiates the mote type'
	from simconf import simconf
	import pyxb

	mote = simconf.moteType()

	mote.breakpoints = ""

	# Location 
	interface_config_type_1 = simconf.interface_configType()
	interface_config_type_1.orderedContent().append(pyxb.binding.basis.NonElementContent("se.sics.cooja.interfaces.Position"))
	interface_config_type_1.x = str(kwargs["x"])
	interface_config_type_1.y = str(kwargs["y"])
	interface_config_type_1.z = "0.0"
	mote.interface_config.append(interface_config_type_1)

	interface_config_type_2 = simconf.interface_configType()
	interface_config_type_2.orderedContent().append(pyxb.binding.basis.NonElementContent("se.sics.cooja.mspmote.interfaces.MspMoteID"))
	interface_config_type_2.id = str(kwargs["motetype_identifier"])
	mote.interface_config.append(interface_config_type_2)

	mote.motetype_identifier = str(kwargs["motetype_identifier"])

	return mote

	

class ioTHoneyNetType(mspl.ioTHoneyNetType):
	'Translates the IoTHoneyNet to Cooja CSC'
	def get_configuration(self):
		from simconf import simconf
		logger.info("processing ioTHoneyNetType to simconf")
		simconf_template_path = 'simconf/simconf-template.csc'
		xml = open(simconf_template_path).read()
		simconf = simconf.CreateFromDocument(xml)

		# Set the iotHonetNet name to simulation
		simconf.simulation.title = self.name

		# Parse the routers
		for router in self.router:
			router.to_simconf(simconf)

		# Parse the honey_pots
		for iot_honey_pot in self.ioTHoneyPot:
			iot_honey_pot.to_simconf(simconf)

		return simconf


class ioTRouterType(mspl.ioTRouterType):
	def to_simconf(self,simconfd):
		logger.info("Parsing Router to simconf")
		obj_type = self.__class__.__name__
		motetype = generate_mote_type(identifier=str(self.id),
							description=self.name,
							source=IoTDEVICE_MODEL[self.model][obj_type]["source"],
							commands=IoTDEVICE_MODEL[self.model][obj_type]["commands"],
							firmware=IoTDEVICE_MODEL[self.model][obj_type]["firmware"],
							mote_interfaces=IoTDEVICE_MODEL[self.model]["mote_interfaces"])
		mote = generate_mote(x=self.location.x,y=self.location.y,motetype_identifier=self.id)
		simconfd.simulation.motetype.append(motetype)
		simconfd.simulation.mote.append(mote)


class ioTHoneyPotType(mspl.ioTHoneyPotType):
	def to_simconf(self,simconfd):
		logger.info("Parsing HoneyPot to simconf")

		obj_type = self.__class__.__name__

		motetype = generate_mote_type(identifier=str(self.id),
							description=self.name,
							source=IoTDEVICE_MODEL[self.model][obj_type]["source"],
							commands=IoTDEVICE_MODEL[self.model][obj_type]["commands"],
							firmware=IoTDEVICE_MODEL[self.model][obj_type]["firmware"],
							mote_interfaces=IoTDEVICE_MODEL[self.model]["mote_interfaces"])

		mote = generate_mote(x=self.location.x,y=self.location.y,motetype_identifier=self.id)

		simconfd.simulation.motetype.append(motetype)
		simconfd.simulation.mote.append(mote)


class M2LPlugin:
	'IoT Controller honeynet Medium to low plugin implementation'

	def get_configuration(self,mspl_source):
		'Return the IoT Controller configuration from the mspl_source'
		# Customize the pyxb generated classes with our own behavior
		global mspl
		mspl.ITResourceType._SetSupersedingClass(ITResourceType)
		mspl.VIoTHoneyNetAction._SetSupersedingClass(VIoTHoneyNetAction)
		mspl.ioTHoneyNetType._SetSupersedingClass(ioTHoneyNetType)
		mspl.ioTRouterType._SetSupersedingClass(ioTRouterType)
		mspl.ioTHoneyPotType._SetSupersedingClass(ioTHoneyPotType)
		
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