import yaml

from testpage import RestHelper
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    username = testdata['username']
    passwd = testdata['password']
    address_login = testdata['address_login']
    address_posts = testdata['address_posts']
    post_title_another_author = testdata['post_title_another_author']
    post_title = testdata['post_title']
    post_description = testdata['post_description']
    post_content = testdata['post_content']


def test_get_post():
    logging.info('Test 1 API is starting')
    rest_session = RestHelper(address_login, username, passwd)
    posts = rest_session.get_post(address_posts)
    assert post_title_another_author in posts, 'Test 1 API fail!'


def test_new_post():
    logging.info('Test 2 API is starting')
    rest_session = RestHelper(address_login, username, passwd)
    new_post = rest_session.new_post(address_posts, post_title, post_description, post_content)
    assert post_description in new_post, 'Test 2 API fail!'

