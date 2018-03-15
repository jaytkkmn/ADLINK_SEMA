# ADLINK_SEMA
#### This python program using ADLINK SEMA eapi tool to get motherboard/system hardware information, and publish those information to MQTT broker, user can monitor motherboard/system status by this program. This project also provide a sample flow.json file for user to create their node-red flow easily.

## Pre-install
1. ADLINK SEMA tool. (SEMA3.5_R7)
2. pip3 install paho-mqtt (For MQTT protocal in python)
3. Python 3.5.2

## Setting
After install SEMA tool, put "json_sema.py" file in /usr/local/SEMA/bin and run this program with root.

## Demo program with docker image
**Create mosquitto by docker** <br>
docker run -td -p 1883:1883 -p 9001:9001 --restart=always --name mosquitto eclipse-mosquitto <br><br>
**Create Node-red environment by docker image** <br>
docker run -td -p 1880:1880 --restart=always --name dockersema --link mosquitto:broker jaytkkmn/adlinksema



