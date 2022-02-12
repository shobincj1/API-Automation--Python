import requests

from features.utilites import RandomnumberGenration, RandomIsle
from features.utilites.Payload import payld


import configparser

config=configparser.ConfigParser()
config.read('Utilities/properties.ini')
print(type(config))


# getAPI= requests.post(parser['API']['baseUrl']+'/Library/Addbook.php',json= payload(488485,3030994))

getAPI=requests.post(config['API']['baseUrl'] +'/Library/Addbook.php', json=payld(RandomnumberGenration.random(), RandomIsle.randomgenIsle()))

assert getAPI.status_code==200

response= getAPI.json()
print(response)
print(response['ID'])
