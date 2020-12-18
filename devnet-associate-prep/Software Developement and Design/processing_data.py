import json
import os
from os import listdir
from os.path import isfile, join

class processing_data:
    def __init__(self,path):
        self.path = path
        self.filepath = self.getFiles()
    
    def getFiles(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            self.filepath = os.path.join(self.path, file)
            return self.filepath
            
    def getJson(self):
        if self.filepath.endswith(".json"):
            #Open the specified database file for reading and perform loading
            with open(self.filepath, 'r') as handler:
                self.data = json.load(handler)
                print(self.data)

if __name__ == "__main__":
    mypath = "devnet-associate-prep\\Software Developement and Design\\data"
    main = processing_data(mypath)
    main.getJson()


