#MV Sense Analytics

#Meraki lib
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.models.object_type_enum import ObjectTypeEnum
from meraki_sdk.exceptions.api_exception import APIException

#Python Lib
import os
import time

class mv_sense:

    def __init__(self):
        self.x_cisco_meraki_api_key = os.environ.get("MERAKI_API_KEY")
        self.serial = os.environ.get("MERAKI_CAM_SERIAL")
        self.object_type = ObjectTypeEnum.PERSON
        self.collect = {}
        self.result_dict = {}

    def configMvSense(self):
        if not self.x_cisco_meraki_api_key:
            raise ValueError("É necessário exportar MERAKI_API_KEY para acessar a API")
        if not self.serial:
            raise ValueError("É necessário exportar MERAKI_CAM_SERIAL para acessar a API")

        self.client = MerakiSdkClient(self.x_cisco_meraki_api_key)

        self.mv_sense_controller = self.client.mv_sense

        #Configuring Opitions
        self.collect['serial'] = self.serial
        self.collect['object_type'] = self.object_type

    def runMvApp(self):
        print("_________________________________")
        print ("*Live*: Dados ao Vivo\n*Recent*: Dados do último minuto\n*Overview*: Dados da última hora")
        print("_________________________________")
        self.menu = int(input('*Menu*\n (1)Live\n (2)Recent\n (3)Overview\nInforme a opção: '))

        if self.menu == 1:
            self.configMvSense()
            self.liveMvSense()

        if self.menu == 2:
            self.configMvSense()
            self.recentsMvSense()
        if self.menu == 3:
            self.configMvSense()
            self.overviewMvSense()

    def recentsMvSense(self):
        #Get recent data of camera (past 1 minute)
        try:
            self.result = self.mv_sense_controller.get_device_camera_analytics_recent(self.collect)
        except APIException as e: 
            print(e)

        for self.di in self.result:
            self.result_dict[self.di['zoneId']] = {}
            for k in self.di.keys():
                if k == 'zoneId' : continue
                self.result_dict[self.di['zoneId']][k]=self.di[k]
        print("_________________________________")
        self.select = int(input("*Zones*\n (1)Full Frame\n (2)Porta - Saida\n (3)Porta - Diego\n (4)Porta - Banheiro\nInforme uma zona: "))

        if self.select == 1:
            print ('A Camera teve {} de entradas no ultimo minuto'.format(self.result_dict[0]['entrances']))
        if self.select == 2:
            print ('A Porta - Saida teve {} de entradas no ultimo minuto'.format(self.result_dict[635570497412661528]['entrances']))
        if self.select == 3:
            print ('A Porta - Diego teve {} de entradas no ultimo minuto'.format(self.result_dict[635570497412661529]['entrances']))
        if self.select == 4:
            print ('A Porta - Saida teve {} de entradas no ultimo minuto'.format(self.result_dict[635570497412661530]['entrances']))

    #Analisar While
    def liveMvSense(self):

        try:
            self.result = self.mv_sense_controller.get_device_camera_analytics_live(self.serial)
        except APIException as e: 
            print(e)
        
        while self.result['zones']['0']['person'] != 0:

            #Cronômetro
            end_time = time.time() + 60
            countTimer = 0
            sleepTime = 1.000
            while time.time() < end_time:
                time.sleep(sleepTime)
                countTimer += sleepTime
                
                if countTimer == 10.0:
                    self.result = self.mv_sense_controller.get_device_camera_analytics_live(self.serial)
                    print (self.result['zones']['0']['person'])
                    break

            if self.result['zones']['0']['person'] == 0:
                break

    def overviewMvSense(self):
        #Get overview data of camera (past 1 hour)
        try:
            self.result = self.mv_sense_controller.get_device_camera_analytics_recent(self.collect)
        except APIException as e: 
            print(e)

        for self.di in self.result:
            self.result_dict[self.di['zoneId']] = {}
            for k in self.di.keys():
                if k == 'zoneId' : continue
                self.result_dict[self.di['zoneId']][k]=self.di[k]
        print("_________________________________")
        self.select = int(input("*Zones*\n (1)Full Frame\n (2)Porta - Saida\n (3)Porta - Diego\n (4)Porta - Banheiro\nInforme uma zona: "))

        if self.select == 1:
            print ('A Camera teve {} de entradas no ultimo minuto'.format(self.result_dict[0]['entrances']))
        if self.select == 2:
            print ('A Porta - Saida teve {} de entradas no ultimo minuto'.format(self.result_dict[635570497412661528]['entrances']))
        if self.select == 3:
            print ('A Porta - Diego teve {} de entradas no ultimo minuto'.format(self.result_dict[635570497412661529]['entrances']))
        if self.select == 4:
            print ('A Porta - Saida teve {} de entradas no ultimo minuto'.format(self.result_dict[635570497412661530]['entrances']))

run = mv_sense()
run.runMvApp()