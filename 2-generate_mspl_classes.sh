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

# Script implementation to generate the mspl classes in python

cd venv_plugins/mspl
#remove all files
rm -rf *.py __* raw
#generate the parser
pyxbgen -u mspl.xsd -m mspl --write-for-customization

rm -rf mspl.py _IoTHoneyNet.py
echo "# -*- coding: utf-8 -*-
import sys
from .raw.mspl import *
from .raw._IoTHoneyNet import *" > __init__.py

# Replace the import in order to find the module
#import _IoTHoneyNet as _ImportedBinding__IoTHoneyNet
sed -i -e 's/import _IoTHoneyNet/from . import _IoTHoneyNet/g' raw/mspl.py
echo "##########################################################"
echo "#                      NEXT STEPS:                       #"
echo "#            ./3-execute_plugin_example.sh               #"  
echo "##########################################################"
