import requests
import json
import os

class Clients:
    
    def __init__(self, uri=None):
        #Definindo URI, caso não seja passado como uma variável de ambiente
        if os.getenv('URI_API') is not None:
            self.uri = os.getenv('URI_API')
        else: 
            self.uri = uri
        
    #Captar todos os usuários
    def getClients(self):
        req = requests.get(self.uri)
        return req

    #Captar o usuário com id especifico
    def getClientsById(self, id):
        uri = self.uri + '/{}'.format(id)
        req = requests.get(uri)
        return req
    
    #Definir um cliente
    def setClient(self, name, email):
        payload = {"name":name, 
                  "email":email}
        req = requests.post(self.uri, json=payload)
        return req
    
    #Alterar um cliente
    def changeClient(self, id, name):
        uri = self.uri + '/{}'.format(id)
        payload = {"name":name}
        req = requests.put(uri, json=payload)
        return req
    
    #Deletar um cliente
    def deleteClient(self, id):
        uri = self.uri + '/{}'.format(id)
        req = requests.delete(uri)
        return req
    
    #Menu principal
    def menu(self):
        option = int(input(' ---=MENU=--- \n 1 - Captar todos os Clientes\n 2 - Captar Cliente por ID\n 3 - Definir Cliente\n 4 - Alterar Cliente \n 5 - Deletar Cliente \n----====----\nOpção: '))

        
        if option == 1:
            res = self.getClients()
            if res.status_code == 200:
                print(res.json())
            else:
                print(res.status_code)
                
        if option == 2:
            id = input('\n ----====---- \n Informe o ID do Cliente que deseja consultar: ')
            res = self.getClientsById(id)
            if res.status_code == 200:
                print(res.json())
            else:
                print(res.status_code)
                
        if option == 3:
            name = str(input('\n ----====---- \n Informe o nome do cliente:'))
            email = str(input('\n ----====---- \n Informe o email do cliente: '))
            res = self.setClient(name, email)
            if res.status_code == 200:
                print(res.json())
            else:
                print(res.status_code)
        
        if option == 4:
            id = input('\n ----====---- \n Informe o ID do Cliente que deseja consultar: ')
            name = str(input('\n ----====---- \n Informe o nome do cliente:'))
            res = self.changeClient(id, name)
            if res.status_code == 200:
                print(res.json())
            else:
                print(res.status_code)
        
        if option == 5:
            id = input('\n ----====---- \n Informe o ID do Cliente que deseja consultar: ')
            res = self.deleteClient(id)
            if res.status_code == 200:
                print(res.json())
            else:
                print(res.status_code)
                
if __name__ == '__main__':
    main = Clients()
    main.menu()