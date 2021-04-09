import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read("D:\\Python\\Udemy_Courses\\rest_api_backend_BDD_python\\personal_api_store_project\\utils\\properties.ini")

    return config

def get_username():
    username = 'user1'

    return username

def get_passcode():
    passcode = 'Bazinga_1'

    return passcode

def get_header():
    headers = {'Content-Type': 'application/json'}

    return headers