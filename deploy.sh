#!/bin/bash

Version="0.0.1"
proxy_host="0.0.0.0"
proxy_port="8888"

echo "Start Goftino_Ai Builder Version $Version";

#sudo apt update && upgrade
#sudo apt install python3 python3-pip

#python3 -m venv ../env
#source ../env/bin/activate

#echo "Installing requirements";
#pip3 install -r requirements.txt
clear

echo "bind gunicorn proxy on port $proxy_host:$proxy_port";
gunicorn --workers 4 --bind $proxy_host:$proxy_port run:app