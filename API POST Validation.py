import json
import os

import requests
import configparser
from Payload import *
print(os.getcwd())
config=configparser.ConfigParser()
config.read('Utilities/properties.ini')
print(config)

postresp = requests.post(config['API']['baseUrl']+'/Library/Addbook.php', json=datatransfer(79979,86868696),
                         headers={'Content-Type': 'application/json'})

assert postresp.status_code == 200

print(type(postresp))
postresp_json = postresp.json()
print(postresp_json)
print(type(postresp_json))
assert postresp_json['Msg'] == "successfully added"

BookId = postresp_json['ID']
print(BookId)

postrespDelete = requests.post(config['API']['baseUrl']+'/Library/DeleteBook.php', json={

    "ID": BookId

}, headers={'Content-Type': 'application/json'})

assert postrespDelete.status_code == 200
postrespDelete_json = postrespDelete.json()
print(postrespDelete_json)
assert postrespDelete_json['msg'] == 'book is successfully deleted'
