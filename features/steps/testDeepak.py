import configparser
import requests
from behave import *

from features.utilites import RandomnumberGenration, RandomIsle
from features.utilites.Payload import payld


@given("endpoint is set")
def step_impl(context):
    context.config1 = configparser.ConfigParser()
    context.config1.read('properties.ini')
    context.host = context.config1['API']['baseUrl']
    print(context.host)


@when("User sends a post request")
def step_impl(context):
    #print(context.host)
    context.getAPI = requests.post(context.host + '/Library/Addbook.php', json=payld(RandomnumberGenration.random(), RandomIsle.randomgenIsle()))


@then("validate the book id")
def book_id_validation(context):

    response = context.getAPI.json()
    print(response)
    print(response['ID'])
    assert context.getAPI.status_code == 200

