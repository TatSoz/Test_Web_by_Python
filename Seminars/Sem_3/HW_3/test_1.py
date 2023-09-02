import time
import yaml

from testpage import OperationsHelper
import logging

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)
    browser_type = testdata['browser']


def test_login_invalid_user(browser):
    """Негативный тест попытки входа на сайт несуществующим пользователем"""
    logging.info('Test 1 is starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    testpage.click_login_button()
    assert testpage.get_error_text() == '401', 'Test 1 fail'


def test_valid_login(browser):
    """Позитивный тест входа на сайт"""
    logging.info('Test 2 is starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()

    testpage.enter_login(testdata['username'])
    testpage.enter_pass(testdata['password'])

    testpage.click_login_button()
    assert testpage.get_login_text() == f'Hello, {testdata["username"]}', 'Test 2 fail'


def test_add_post(browser):
    """Позитивный тест добавления поста"""
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

    assert testpage.get_post_title() == testdata['post_title'], 'Test 3 fail'


def test_contact_us(browser):
    logging.info('Test 4 is starting')
    testpage = OperationsHelper(browser)
    testpage.click_contact_button()
    time.sleep(testdata['sleep_time'])
    testpage.enter_your_name_contact_us(testdata['username'])
    testpage.enter_your_mail_contact_us(testdata['email'])
    testpage.enter_content_contact_us(testdata['content_to_contact_us'])
    testpage.click_contact_us_button()
    time.sleep(testdata['sleep_time'])
    assert testpage.get_alert_contact_us() == 'Form successfully submitted', 'Test 4 fail'