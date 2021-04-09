import requests, json, pprint
from behave import *
from utils.API_resources import ApiResources
from utils.configurations import *

@given('the user details <username> and <password> are provided for login')
def set_login(context):
    context.url = get_config()['API']['endpoint']
    context.resource = ApiResources.user_login
    context.json_data = {'username': get_username(),
                         'password': get_passcode()
                         }

    print(get_username(),get_passcode())
    context.header = json.loads(get_config()['API']['header'])

@when('we executed the login API Method')
def set_login(context):
    context.request_login = requests.post(context.url+context.resource,
                                          json=context.json_data,
                                          headers=context.header
                                          )

@then('user should able to login successfully')
def set_login(context):
    response_login = context.request_login.json()

    print("' Login_Status_Code'", context.request_login.status_code)
    pprint.pprint(response_login)

    context.access_code = response_login['access_token']
    context.refresh_code = response_login['refresh_token']

    print(context.access_code)

