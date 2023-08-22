import requests
import yaml

S = requests.Session()
with open('config.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address = data['address_posts']



def test_rest(user_login, post_title):
    res = S.get(url=address, headers={'X-Auth-Token': user_login}, params={'owner': 'notMe'}).json()['data']
    r =[i['title'] for i in res]
    assert post_title in r, 'Test_1 Fail'


def test_new_post(user_login, new_post):
    S.post(url=address, headers={'X-Auth-Token': user_login}, data={'title': new_post[0],
                                                                    'description': new_post[1], 'content': new_post[2]})
    res = S.get(url=address, headers={'X-Auth-Token': user_login}).json()['data']
    r = [i['description'] for i in res]
    assert new_post[1] in r, 'Test_2 Fail'
