# ANASTACIA H2020 Plugin Development Environment Generator

## Introduction

This software allows auto-generate an ANASTACIA plugin development environment. It has been developed by the Department of Information and Communications Engineering of the University of Murcia under ANASTACIA H2020 European project.
http://anastacia-h2020.eu/

## Installation
The software has been developed in python so we recommend the use of virtualenv.

- Install the virtualenv (depends on your distribution)
	- sudo apt-get install virtualenv
- Generate the virtual env:
	- ./1-generate_plugin_env.sh
- Activate the generated virtual environment (IMPORTANT!):
	- source venv_plugins/bin/activate
- Generate the mspl classes (ignore the warnings):
	- ./2-generate_mspl_classes.sh
- Execute the plugin example:
	- ./3-execute_plugin_example.sh

## Team
This software has been developed by the Department of Information and Communications Engineering of the University of Murcia.
@author: alejandro.mzarca@um.es