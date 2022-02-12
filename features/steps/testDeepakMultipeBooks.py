import configparser

import requests
from behave import *

from features.utilites.Payload import payld

use_step_matcher("re")


@when("User sends a post request with (?P<isbn>.+) and (?P<aisle>.+)")
def step_impl(context, isbn, aisle):
    print(context.host)
    context.getAPI = requests.post(context.host + '/Library/Addbook.php', json=payld(isbn, aisle))
