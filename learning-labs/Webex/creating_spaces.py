import requests
import json
requests.packages.urllib3.disable_warnings()

class manage_spaces():

    def __init__(self):
      self.endpoint = "https://api.ciscospark.com/v1/"
      self.resource = " "
      self.subresource = " "
      self.menu_opcao = " "
      self.url = " "
      self.access_token = " "
      self.headers = " "
      self.payload = " "
      self.person =  " "
      self.response = " "
    

    def menu(self):
      self.access_token = (input("Informe o token para iniciar: \n"))
      self.headers = {'Authorization': 'Bearer ' + self.access_token, 'Content-Type': 'application/json'}

      self.resource = input("Qual o Recurso voce quer usar? (rooms, messages): \n")

      if self.resource == "rooms":
        self.rooms()
      if self.resource == "messages":
        self.messages()

    def rooms(self):
      print ("-----  Opcoes  -----")
      self.menu_opcao = input("1 - List Rooms \n2 - Create a Room \n3 - Delete a Room\nOpcao: ")
      print ("--------------------")
      #Listando as salas
      if self.menu_opcao == "1":
        self.subresource = input("Qual tipo de sala? (direct or group)\n")
        #Setando o tipo de sala
        if self.subresource == "direct":
          self.subresource = "?type=direct"
          self.url = self.endpoint + self.resource + self.subresource

        if self.subresource == "group":
          self.subresource = "?type=group"
          self.url = self.endpoint + self.resource + self.subresource

      #Gerando Json 
      self.response = requests.get(self.url, headers = self.headers, verify=False).json()
      
      self.person = self.response["items"][0]

      print ("Name: "  + self.person["title"])
      print ("Type: " + self.person["type"])
    
    def messages(self):
      print ("--------------------")
      print ("404 - Not Found")
      print ("--------------------")

main = manage_spaces()
main.menu()



