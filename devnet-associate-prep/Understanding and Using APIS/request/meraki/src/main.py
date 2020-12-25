import requests
import os 

#d7513b1e346e7e6be161548f93ef2d6939049f76
class processMerakiData:
    def __init__(self):
        self._meraki_api_key = os.getenv('MERAKI_API_KEY')
        self.headers = {'X-Cisco-Meraki-API-Key': self._meraki_api_key}
        self.api_uri = 'https://api.meraki.com/api/v0/'
    
    def getOrganizations(self):
        url = self.api_uri + 'organizations'
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code
        
    def getNetworksByOrganization(self, org_id):
        for org in org_id:
            response = requests.get('{}{}/{}{}'.format(self.api_uri, 'organizations', org, '/networks/'), headers=self.headers)
            if response.status_code == 200:
                return response.json()
            else:
                return response.status_code
                
    def getNetworkDevices(self, network_id):
        for networkid in network_id:
            response = requests.get('{}{}/{}{}'.format(self.api_uri, 'networks', networkid, '/devices/'), headers=self.headers)
            if response.status_code == 200:
                print (response.json)
            else:
                print (response.status_code)
        
    def setNetworkId(self):
        networks = self.getNetworksByOrganization(self.setOrgByName('Betha'))
        networks_id = []
        for network in networks:
            networks_id.append(network.get('id'))
        return networks_id
        
    def setOrgByName(self, name):
        organizations = self.getOrganizations()
        org_id = []
        for org in organizations:
            if name.lower() in org.get('name').lower():
                org_id.append(org.get('id'))
        return org_id 

if __name__ == '__main__':
    main = processMerakiData()
    