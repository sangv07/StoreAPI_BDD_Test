import requests, json

from behave import *
from requests.auth import HTTPBasicAuth

from utils import configurations, API_resources

tags = []
def after_tag(context, tag):

    tags.append(tag)
    print("****TAG_Enviornemnt**** ", tags)

# make sure to execute one Login Scenario ran
    if tag == 'login':

        config = configurations.get_config()
        resource = API_resources.ApiResources.user
        url = config['API']['endpoint']
        access_token = context.access_code
        refresh_token = context.refresh_code
        print(type(access_token))


        # headers = {"Content-Type": "application/json",
        #            "Authorization": "Bearer " + access_token
        #            }
# OR Below method
# first converting String to DICT
        headers = json.loads(config['API']['auth'])
        headers['Authorization'] = "Bearer " + access_token
        print(headers)

        request_delete = requests.delete(url=url + resource.format(user_id=1),
                                         headers=headers,
                                         verify=False,
                                         #auth=HTTPBasicAuth(access_token + "Bearer ")
                                         #auth=access_token
                                         )

        print(access_token)

        print('code_delete', request_delete.status_code)
        print(url+resource.format(user_id=1))
        response_delete = request_delete.json()
        print(response_delete)

