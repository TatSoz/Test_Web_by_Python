import pytest
import requests
import yaml


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address = data['username'], data['password'], data['address']

S = requests.Session()


@pytest.fixture()
def correct_word():
    return 'молоко'


@pytest.fixture()
def incorrect_word():
    return 'малако'


@pytest.fixture()
def user_login():
    S.post(url=address, data={'username': username, 'password': password})
    return rest1.json()
