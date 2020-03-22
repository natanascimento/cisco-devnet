import requests
import json

class manage_mvsense:

    def __init__(self):
        self.urlbase = "https://api.meraki.com/api/v0/devices/"
        self.headers = {'X-Cisco-Meraki-API-Key': '8c852b04950e9a44e9c7ab3396462d7b9417fe4b', 'Content-Type': 'application/json'}
        self.payload = {}
        self.url = " "

    def runBase (self):
        serial = "Q2EV-ALRC-2U8N"
        self.urlbase = self.urlbase + serial + "/camera/analytics/"
    
    def runAnalysis (self):
        #Rodando a Geração da URL base
        self.runBase()

        #Iniciando coletas de parâmetros
        inp = input(" ## Parametro (Z = Zones, O = Overview): ")
        print ("-------------------")

        if inp == "Z" or inp == "z":
            self.url = self.urlbase + 'zones'
        if inp == "O" or inp == "o":
            self.url = self.urlbase + 'overview'
        
        self.response = requests.request("GET", self.url, headers=self.headers, data = self.payload)

        #Analisando o estado da requisição
        self.state = self.response.status_code
        if self.state == 404:
            print ("Error 404")

        #Transformando o output da requisição
        self.data = json.loads(self.response.text.encode('utf-8'))

    def captandoIdZones (self):
        for self.item in self.data:
            self.id = {self.item['label']:self.item['zoneId']}
            print (self.id)
            

run = manage_mvsense()
run.runAnalysis()
run.captandoIdZones()