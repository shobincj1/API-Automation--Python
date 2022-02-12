import requests
from behave import *

from features.utilites import RandomnumberGenration, RandomIsle
from features.utilites.Payload import payld

use_step_matcher("re")
import configparser

@given("Add Book API is executed")
def step_impl(context):
    context.confg=configparser.ConfigParser()
    context.confg.read('Utilities/properties.ini')
    context.getAPI=requests.post(context.confg['API']['baseUrl'] +'/Library/Addbook.php', json=payld(RandomnumberGenration.random(), RandomIsle.randomgenIsle()))
    assert context.getAPI.status_code==200
    context.response= context.getAPI.json()
    context.bkID=context.response['ID']

# print(response)
# print(response['ID'])


@when("User searches for added book")

def step_impl(context):
    context.getbk=requests.get(context.confg['API']['baseUrl']+'/Library/GetBook.php',params={"ID":context.bkID})



@then("User is able to find the search")
def step_impl(context):
    jsngetbk = context.getbk.json()
    print(jsngetbk)
