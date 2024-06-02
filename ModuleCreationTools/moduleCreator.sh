#!/usr/bin/bash

name=$1

mkdir ../KrakenModules/$name
cp ./templateFiles/main.py ../KrakenModules/$name/main.py
cp ./templateFiles/module.ini ../KrakenModules/$name/module.ini
