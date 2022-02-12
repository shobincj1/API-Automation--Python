import json
import requests
import configparser

config = configparser.ConfigParser()
config.read('Utilities/properties.ini')
Newurl=config['Auth']['url']
response = requests.get(Newurl,verify=False,auth=('shobincj@gmail.com','Manayil@1982'))
response.json()
print(response.json())
