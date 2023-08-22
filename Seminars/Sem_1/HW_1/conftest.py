import pytest
import requests
import yaml


with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    username, password, address_login = data['username'], data['password'], data['address_login']

S = requests.Session()

@pytest.fixture()
def user_login():
    rest1 = S.post(url=address_login, data={'username': username, 'password': password})
    return rest1.json()['token']


@pytest.fixture()
def post_title():
    return 'Море'

@pytest.fixture()
def new_post():
    title = 'Crazy House'
    description = 'Самой известной и посещаемой достопримечательностью Далата является отель под названием Crazy House.'
    content = ('Сумасшедший дом (Crazy House, Hang Nga Hotel) – это одновременно отель и музей, который находится в '
               'Далате. Объект представляет собой целый комплекс зданий необычной архитектуры, полностью построенный '
               'из бетона. Даже огромные стволы деревьев, под которые стилизовано строение, тоже выполнены из прочного '
               'бетонного материала. Необычный дизайн и отсутствие прямых углов делают Крейзи хаус уникальным объектом, '
               'привлекающим туристов. К тому же, вы можете не только осмотреть это необычное место, '
               'но и остаться на ночь в одном из номеров отеля.')
    return title, description, content


