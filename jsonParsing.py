

import json

file = open('C:\\Users\\19732\\AppData\\Local\\Programs\\Python\\Python310\\Test Scripts\\SAMPLE.txt')


dict_sample=json.load(file)

dict_batters=dict_sample['batters']
print(dict_batters['batter'])

for i in range(len(dict_batters['batter'])):
               if dict_batters['batter'][i]['id']=='1002':
                   print(dict_batters['batter'][i]['type'])

file1 = open('C:\\Users\\19732\\AppData\\Local\\Programs\\Python\\Python310\\Test Scripts\\SAMPLE2.txt')


dict_sample1=json.load(file1)

assert dict_sample1==dict_sample
