#MV Sense Analytics (Refatorado para AWS Lambda)

#Meraki lib
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.models.object_type_enum import ObjectTypeEnum
from meraki_sdk.exceptions.api_exception import APIException

def mainMvSense():
    x_cisco_meraki_api_key = '8c852b04950e9a44e9c7ab3396462d7b9417fe4b'
    serial = 'Q2EV-ALRC-2U8N'
    object_type = ObjectTypeEnum.PERSON
    collect = {}
    result_dict = {}
    client = MerakiSdkClient(x_cisco_meraki_api_key)

    mv_sense_controller = client.mv_sense

    #Configuring Opitions
    collect['serial'] = serial
    collect['object_type'] = object_type

    try:
        result = mv_sense_controller.get_device_camera_analytics_recent(collect)
    except APIException as e: 
        print(e)

    for di in result:
        result_dict[di['zoneId']] = {}
        for k in di.keys():
            if k == 'zoneId' : continue
            result_dict[di['zoneId']][k]=di[k]
        
    return (result_dict)


