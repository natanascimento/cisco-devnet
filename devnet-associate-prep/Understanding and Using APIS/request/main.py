import requests
import json

uri = 'http://localhost:3000/clients/15'

r = requests.get(uri)

if r.status_code == 200:
    print(r.json())
else:
    print(r.status_code)
