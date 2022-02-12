import os

# loc=open('C:\\Users\\19732\\AppData\\Local\\Programs\\Python\\Python310\\Test Scripts\\SAMPLE.txt')
#
# dicfileoutput= json.load(loc)
# print(dicfileoutput)
# print(dicfileoutput['name'])
# dict_batters=dicfileoutput['batters']
# # print(dict_batters)
# # print(type(dict_batters))
# list_batter=dict_batters['batter']
#
# print(list_batter)
#
# # range(list_batter)
# # for ing in list_batter:
# # 	if (ing['type']=='Chocolate'):
# # 		print(ing['id'])

#
# lst1=[2,5,6,5,7]
# print(range(1,len(lst1),2))
#
# for i in range(1,len(lst1),3):
# 	print(lst1[i])

#
# file = open("C:\\Users\\19732\\AppData\\Local\\Programs\\Python\\Python310\\Test Scripts\\SAMPLE.txt")
# contents=json.load(file)

# with open("C:\\Users\\19732\\AppData\\Local\\Programs\\Python\\Python310\\Test Scripts\\SAMPLE.txt") as fp:
# 	contents = json.load(fp)
# print(contents)
# dict_batters=contents['batters']
# print(dict_batters)
# lst_batter=dict_batters['batter']
# print(lst_batter)
#
# for i in lst_batter:
#
# 	if i['type'] =='Regular':
# 		print(i['id'])

import configparser
print(os.getcwd())
from features.utilites import Payload

config=configparser.ConfigParser()
config.read("Utility/property.ini")
# config.read('Utilities/properties.ini')
print(config)

import requests

response=requests.post(config['API']['baseUrl'] +'/Library/Addbook.php', json=Payload.payld(665456, 45545))
# response=requests.post('http://216.10.245.166/Library/Addbook.php',json=Payload.payld(2233,45545))
jsonresp=response.json()
print(response.content)
print(jsonresp)
print(type(jsonresp))
bkID=jsonresp['ID']
print(bkID)



getbk=requests.get(config['API']['baseUrl']+'/Library/GetBook.php',params={"ID":bkID})
jsngetbk=getbk.json()
print(jsngetbk)

dltbk=requests.post(config['API']['baseUrl'] +'/Library/DeleteBook.php', json=Payload.delbk(bkID))
jsndltbk=dltbk.json()
print(jsndltbk)


# import mysql
# dbconnect=mysql.connector.Connect
# cursor=dbconnect.c