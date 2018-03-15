#!/usr/bin/python3
import json
import time
import paho.mqtt.publish as publish
from subprocess import check_output


def mqtt_pub(topic, payload):
    """Use MQTT to publish the data"""

    host = "localhost"
    publish.single(topic, payload, qos=1, hostname=host)


def get_info(semadata):
    """Get information by SEMAEApi and use subprocess->check_output to capture result"""

    semadata['Board_Name'] = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetStringA", str(2)]).decode("utf-8")
    semadata['BIOS_Revision'] = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetStringA", str(4)]).decode("utf-8")

    semadata['CPU_Info'] = check_output(["./semaeapi_tool", "-a", "SemaEApiCPUGetString", "1"]).decode("utf-8")
    semadata['Number_of_CPUs'] = check_output(["./semaeapi_tool", "-a", "SemaEApiCPUGetValue", str(3)]).decode("utf-8")
    semadata['Number_of_cores'] = check_output(["./semaeapi_tool", "-a", "SemaEApiCPUGetValue", str(4)]).decode("utf-8")

    return semadata


def get_realtime_info(semadata):
    """Get information by SEMAEApi and use subprocess->check_output to capture result"""

    semadata['CPU_Temp'] = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetValue", str(8)]).decode("utf-8")
    semadata['System_Temp'] = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetValue", str(10)]).decode("utf-8")
    semadata['CPU_Core_Voltage'] = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetValue", str(11)]).decode("utf-8")
    semadata['CPU_Fan'] = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetValue", str(18)]).decode("utf-8")
    semadata['memory_frequency'] = check_output(["./semaeapi_tool", "-a", "SemaEApiMemoryGetValue", str(1)]).decode("utf-8")
    semadata['total_size'] = check_output(["./semaeapi_tool", "-a", "SemaEApiMemoryGetValue", str(2)]).decode("utf-8")
    semadata['free_memory'] = check_output(["./semaeapi_tool", "-a", "SemaEApiMemoryGetValue", str(3)]).decode("utf-8")

    return semadata


topic = 'SEMA'
semadata = {'Board_Name':'',
            'BIOS_Revision':'',
            'CPU_Info':'',
            'CPU_Temp':'',
            'System_Temp':'',
            'CPU_Core_Voltage':'',
            'CPU_Fan':'',
            'Number_of_CPUs':'',
            'Number_of_cores':'',
            'memory_frequency':'',
            'total_size':'',
            'free_memory':''
            }

msg = get_info(semadata)

while True:
    time.sleep(1)
    """Refresh realtime data every 1 second"""

    msg = get_realtime_info(msg)
    msg_json = json.dumps(msg)
    mqtt_pub(topic, msg_json)
