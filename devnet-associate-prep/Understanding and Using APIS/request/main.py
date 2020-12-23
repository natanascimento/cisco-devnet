import requests
import json

class Clients:
    
    def __init__(self):
        self.uri = "http://localhost:3000/clients"
        
    def getClients(self):
        req = requests.get(self.uri)
        return req

    def getClientsById(self, id):
        uri = self.uri + '/' + id
        req = requests.get(uri)
        return req
    
    def menu(self):
        option = int(input(' ---=MENU=--- \n 1 - Captar todos os Clientes\n 2 - Captar Cliente por ID\n ----====----\nOpção: '))

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

if __name__ == '__main__':
    main = Clients()
    main.menu()