import json
import os
from os import listdir
from os.path import isfile, join
#External Library
import yaml
import xmltodict

class processing_data:
    def __init__(self,path):
        self.path = path
    
    def getFiles(self):
        files = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        for file in files:
            if file.endswith(".json"):
                filepath_json = os.path.join(self.path, file)
                print(filepath_json)
                self.getJsonData(filepath_json)
            elif file.endswith(".yaml"):
                filepath_yaml = os.path.join(self.path, file)
                print(filepath_yaml)
                self.getYamlData(filepath_yaml)
            elif file.endswith(".xml"):
                filepath_xml = os.path.join(self.path, file)
                print(filepath_xml)
                self.getXMLData(filepath_xml)

            
    def getJsonData(self,filepath):
        #Open the specified database file for reading and perform loading
        with open(filepath, 'r') as handle:
            data_json = json.load(handle)
            print(data_json)
    
    def getYamlData(self, filepath):
        #Open the specified database file for reading and perform loading
        with open(filepath, 'r') as handle:
            data_yaml = yaml.safe_load(handle)
            print(data_yaml)
            
    def getXMLData(self, filepath):
        #Open the specified database file for reading and perform loading
        with open(filepath, 'r') as handle:
            data_xml = xmltodict.parse(handle.read())["root"]
            print(data_xml)
            
if __name__ == "__main__":
    mypath = "data"
    main = processing_data(mypath)
    main.getFiles()


