import os

print("Current Dir- C:\\Users\19732\\PycharmProjects\\BackEndAutomation\\Revision")
print(os.getcwd())

print("Parent Dir- C:\\Users\\19732\\PycharmProjects\\BackEndAutomation")
parent_folder = os.path.dirname(os.getcwd())
print(parent_folder)

print('Super Parent Dir- C:\\Users\\19732\\PycharmProjects')
print(os.path.dirname(parent_folder))
SuperParent = os.path.dirname(parent_folder)
print(SuperParent)

filename = parent_folder + '\\Payload.py'
print(filename)
exec(open(filename).read())

# os.chdir(parent_folder)
# os.getcwd()
#
#filename = parent_folder + '\\Utilities\\property.ini'
# print(filename)
#
# config = configparser.ConfigParser()
# config.read(filename)
# getAPI = requests.post(config['API']['baseUrl'] + '/Library/Addbook.php', json=payload(56776796, 3030994))
#
# print(getAPI)
# #
# # response = requests.post(
# #
# # )