import time
import yaml

from testpage import OperationsHelper
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_type = testdata['browser']


def test_login_invalid_user(browser):
    logging.info('Test 1 is starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()

    testpage.enter_login('test')
    testpage.enter_pass('test')

    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'Test 1 failed'


def test_valid_login(browser):
    logging.info('Test 2 is starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()

    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])

    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username"]}', 'Test 2 failed'


def test_add_post(browser):
    logging.info('Test 3 is starting')
    testpage = OperationsHelper(browser)

    time.sleep(testdata['sleep_time'])
    testpage.click_create_post_button()
    time.sleep(testdata['sleep_time'])

    testpage.enter_post_title(testdata['post_title'])
    testpage.enter_post_description(testdata['post_description'])
    testpage.enter_post_content(testdata['post_content'])

    testpage.click_save_post_button()
    time.sleep(testdata['sleep_time'])

    assert testpage.get_post_title() == testdata['post_title'], 'Test 3 failed'



