#!/bin/bash

#__author__ = "Alejandro Molina Zarca"
#__copyright__ = "Copyright 2018, ANASTACIA H2020"
#__credits__ = ["Antonio Skarmeta", "Alejandro Molina Zarca"]
#__license__ = "GPL"
#__version__ = "0.0.1"
#__maintainer__ = "Alejandro Molina Zarca"
#__email__ = "alejandro.mzarca@um.es"
#__status__ = "Development"

# Script implementation to generate the venv environment in order to test
# the security enabler plugins

echo "Generating environment..."
# Generating a python3 venv
virtualenv -p python3 venv_plugins
#Activate the venv
source venv_plugins/bin/activate
#Install the pyxb in the venv
pip3 install PyXB==1.2.6
# create the structure folders for the plugin
mkdir venv_plugins/m2l_plugins
mkdir venv_plugins/mspl
cp -r *.py test mspl_cooja venv_plugins/m2l_plugins
cp mspl.xsd venv_plugins/mspl
cp iot-honeynet.xsd venv_plugins/mspl

echo "##########################################################"
echo "#                      WARNING!!!!!!!                    #"
echo "#           THE PLUGINS FOR DEVELOPMENT ARE              #"
echo "#                       NOW IN:                          #"
echo "#           ---> venv_plugins/m2l_plugins <---           #"
echo "##########################################################"
echo ""
echo "##########################################################"
echo "#                      NEXT STEPS:                       #"
echo "#            source venv_plugins/bin/activate            #"  
echo "#            ./2-generate_mspl_classes.sh                #" 
echo "##########################################################"

