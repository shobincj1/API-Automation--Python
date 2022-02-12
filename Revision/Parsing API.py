import json
import requests

loc=open('C:\\Users\\19732\\AppData\\Local\\Programs\\Python\\Python310\\Test Scripts\\SAMPLE.txt')
contnt=json.load(loc)
print(contnt)
print(type(contnt))

dict_batters=contnt['batters']
print(dict_batters)

list_batter=dict_batters['batter']
print(list_batter)

for ingdt in list_batter:
    if ingdt['id']=='1002':
        print(ingdt['type'])