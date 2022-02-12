import mysql.connector
import configparser
from mysql.connector import errors

import properties as properties

import Utilities
from Utilities import *

config=configparser.ConfigParser()
config.read(Utilities/properties.ini)

dbproperties={
    'user' : config['SQL']['user'],
    'password':config['SQL']['password'],
    'host':config['SQL']['password'],
    'database':config['SQL']['database']
}

def dbconnect():
    try:
        connect = mysql.connector.connect(**dbproperties)
        if connect.is_connected()==True:
            print('DB Connection is successfull')
            return connect

    except errors as e:
        print(e)