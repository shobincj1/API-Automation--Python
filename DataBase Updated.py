import mysql.connector


# connect=mysql.connector.connect(host='localhost',database='PythonAutomation',user='root',password='Manayil@1982')
from Utilities.Configuartion import *

connect = dbconnect()

print(connect.is_connected())
cursor = connect.cursor()

cursor.execute('select * from CustomerInfo')

results = cursor.fetchall()
print(type(results))
sum = 0
for eachelement in results:
    print(eachelement[2])
    # print(type(eachelement[2]))
    sum = sum + eachelement[2]
print(sum)
