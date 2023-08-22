import requests
import yaml


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address = data['username'], data['password'], data['address']

S = requests.Session()


def user_login():
    rest1 = S.post(url=address, data={'username': username, 'password': password})
    return rest1.json()


print(user_login())

