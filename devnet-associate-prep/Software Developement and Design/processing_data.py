import json
import os
from os import listdir
from os import path
from os.path import isfile, join

class processing_data:
    def __init__(self):
        self.filepath = self.getFiles()
     
    def verifying_path(self, path):
        if os.path.isdir(self.path):
            self.path = path
            self.getFiles(self.path)
    
    def getFiles(self, path):
        files = [f for f in listdir(path) if isfile(join(path, f))]
        for file in files:
            self.filepath = os.path.join(path, file)
            return self.filepath
            
    def getJson(self):
        if self.filepath.endswith(".json"):
            #Open the specified database file for reading and perform loading
            with open(self.filepath, 'r') as handler:
                self.data = json.load(handler)
                print(self.data)

if __name__ == "__main__":
    mypath = "devnet-associate-prep\\Software Developement and Design\\data"
    main = processing_data()
    main.verifying_path(mypath)


