import json
import os
from os import listdir
from os.path import isfile, join
#External Library
import yaml

class processing_data:
    def __init__(self,path):
        self.path = path
        #self.filepath = self.getFiles()
    
    def getFiles(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            if file.endswith(".json"):
                filepath_json = os.path.join(self.path, file)
                print(filepath_json)
                self.getJson(filepath_json)
            elif file.endswith(".yaml"):
                filepath_yaml = os.path.join(self.path, file)
                print(filepath_yaml)
                self.getYaml(filepath_yaml)

            
    def getJson(self,filepath):
        #Open the specified database file for reading and perform loading
        with open(filepath, 'r') as handle:
            data_json = json.load(handle)
            print(data_json)
    
    def getYaml(self, filepath):
        #Open the specified database file for reading and perform loading
        with open(filepath, 'r') as handle:
            data_yaml = yaml.safe_load(handle)
            print(data_yaml)

if __name__ == "__main__":
    mypath = "data"
    main = processing_data(mypath)
    main.getFiles()


