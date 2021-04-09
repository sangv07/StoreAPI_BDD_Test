import requests, json
from behave import *
from utils import API_resources, configurations


resource = API_resources.ApiResources
config = configurations.get_config()
passcode = configurations.get_passcode()

@given('the user detail which {username} and {password} need to be added to db')
def step_register(context, username, password):
    context.url = config['API']['endpoint']
    context.resource = resource.user_register
    context.header = config['API']['header']
    abc = json.loads(context.header)
    print(type(abc))
    print(abc)
    context.body = {'username': username,
                    'password': password
                    }

@when('we executed the user_register API Method')
def step_register(context):
    context.response_register = requests.post(context.url + context.resource,
                                              json=context.body,
                                              headers=json.loads(context.header)
                                              )

@then('User should successfully registered')
def step_register(context):
    response_json = context.response_register.json()

    print(context.response_register)
    print(response_json)

    assert response_json['Msg'] == 'User Register Successfully /users/post'