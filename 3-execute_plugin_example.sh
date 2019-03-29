#!/bin/bash

#!/bin/bash

#__author__ = "Alejandro Molina Zarca"
#__copyright__ = "Copyright 2018, ANASTACIA H2020"
#__credits__ = ["Antonio Skarmeta", "Alejandro Molina Zarca"]
#__license__ = "GPL"
#__version__ = "0.0.1"
#__maintainer__ = "Alejandro Molina Zarca"
#__email__ = "alejandro.mzarca@um.es"
#__status__ = "Development"

# Script implementation to test the current plugin implementations

cd venv_plugins/m2l_plugins

# Executes the main method in mspl_onos_nb to translate the proactive and reactive policies
python3 mspl_onos_nb.py test/iot_registration/proactive/fwd-pana-dst.xml
python3 mspl_onos_nb.py test/iot_registration/proactive/fwd-pana-src.xml
python3 mspl_onos_nb.py test/iot_registration/reactive/fwd-broker-to-iot.xml
python3 mspl_onos_nb.py test/iot_registration/reactive/fwd-iot-to-broker.xml

# Executes the main method in mspl_iptables example using the filtering example
python3 mspl_ovs-fw.py test/MEC3/filtering-MEC3.xml

# Executes the main method in mspl_odl example using the filtering example
python3 mspl_ovs-fw.py test/BMS3/filtering-BMS3.xml

# Executes the main method in mspl_iot_controller example using the dtls example
python3 mspl_iot_controller.py test/BMS4/iot-control-BMS4.xml

# Executes the main method in mspl_cooja example using the iot-honeynet example
cd mspl_cooja
python3 mspl_cooja.py ../test/BMS2/iot-control-honeynet-BMS2.xml




