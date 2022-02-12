from behave import *
import requests
import configparser


@given('the book details are given')
def stepimpl(context):

    context.config = configparser.ConfigParser()
    context.config.read('Utilities/properties.ini')
    # print(type(config))

@when('Add Book API is executed')
def step_impl(context):
    postresp = requests.post(context.config['API']['baseUrl']+'/Library/Addbook.php', json=datatransfer(6306096),
                             headers={'Content-Type': 'application/json'})
    assert postresp.status_code == 200
    context.postresp_json = postresp.json()




@then('book is successfully added')
def step_impl(context):
    assert context.postresp_json['Msg'] == "successfully added"

