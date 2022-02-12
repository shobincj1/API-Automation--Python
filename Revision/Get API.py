import requests
import os

from features.utilites.Payload import *

import configparser

print(os.getcwd())

parentdir = os.path.dirname(os.getcwd())
print(parentdir)
filename = parentdir+'/Utilities/property.ini'
print(filename)
config = configparser.ConfigParser()
config.read(filename)
print(type(config))

# getAPI= requests.post(parser['API']['baseUrl']+'/Library/Addbook.php',json= payload(488485,3030994))

getAPI = requests.post(config['API']['baseUrl'] + '/Library/Addbook.php', json=payld(56776796,90994))

assert getAPI.status_code == 200

response = getAPI.json()
print(response)
print(response['ID'])
