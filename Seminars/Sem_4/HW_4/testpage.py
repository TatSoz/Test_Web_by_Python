from json import JSONDecodeError

from selenium.common import TimeoutException

from BaseApp import BasePage, BaseRest
from selenium.webdriver.common.by import By
import logging
import yaml


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)
        for locator in locators['xpath'].keys():
            ids[locator] = (By.XPATH, locators['xpath'][locator])
        for locator in locators['css'].keys():
            ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])

class OperationsHelper(BasePage):

    def enter_text_into_field(self, locator, word, description=None):
        """Вспомогательная функция обработки Exceptions ввода"""
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send {word} to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except TimeoutException:
            logging.exception(f'Exception while operation with {locator}')
            return False
        return True

    def click_button(self, locator, description=None):
        """Вспомогательная функция обработки Exceptions клика по кнопке"""
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except TimeoutException:
            logging.exception('Exception with click')
        logging.debug(f'Clicked {element_name} button')
        return True


    def get_text_from_element(self, locator, description):
        """Вспомогательная функция обработки Exceptions получение текста"""
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except TimeoutException:
            logging.exception(f'Exception while get test from {element_name}')
            return None
        logging.debug(f'We find text {text} in field {element_name}')
        return text


# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description='Enter the login')


    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description='Enter the password')


    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FORM_POST_TITLE"], word, description='Title new post')

    def enter_post_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FORM_POST_DESCRIPTION"], word, description='Description new post')


    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_FORM_POST_CONTENT"], word, description='Content new post')


    def enter_your_name_contact_us(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_NAME_CONTACT_US"], word, description='Enter your name in Contact Us form')


    def enter_your_mail_contact_us(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_YOUR_EMAIL_CONTACT_US"], word, description='Enter your email in Contact Us form')


    def enter_content_contact_us(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_CONTACT_US"], word, description='Enter content in Contact Us form')


# CLICK
    def click_login_button(self):
       self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description='Click login button')

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description='Click creating post button')

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_POST_BTN"], description='Click saving post button')


    def click_contact_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_OPEN_FORM_CONTACT_BTN"], description='Click on the button Contact')

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description='Click on the button CONTACT US')


# GET TEXT
    def get_error_text(self):
        """Ищет элемент с оповещением об ошибке и получает атрибут text"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description='Get error text')


    def get_login_text(self):
        """Возврат имени пользователя"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_USER_PROFILE_LINK"], description='Get text profile')


    def get_post_title(self):
        """Возврат названия поста пользователя"""
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_POST_NAME"], description='Get title post')

    def get_alert_contact_us(self):
        """Получение текста подстерждение действия на странице """
        logging.info('Get text alert')
        text = self.get_alert_text()
        logging.info(text)
        return text


class RestHelper(BaseRest):

    def get_token(self):

        token = ''
        try:
            token = self.user_login()
        except KeyError:
            logging.exception(f'Failed user {self.username} login')
        except JSONDecodeError:
            logging.exception(f'404 not found!')

        return token

    def get_post(self, address_posts):

        logging.info('Getting list of posts...')

        token = self.get_token()
        results = []

        try:
            data = self.session.get(url=address_posts,
                                    headers={'X-Auth-Token': token},
                                    params={'owner': 'notMe'}).json()['data']
            results = [i['title'] for i in data]
        except KeyError:
            logging.exception('Invalid token in GET request')

        if len(results) > 0:
            logging.info('Success')
        else:
            logging.info('No posts!')

        return results

    def new_post(self, address_posts, title, description, content):
        logging.info('Creating a new post...')

        token = self.get_token()
        descriptions = []
        try:
            self.session.post(url=address_posts,
                              headers={'X-Auth-Token': token},
                              data={'title': title, 'description': description, 'content': content})
            posts_info = self.session.get(url=address_posts,
                                          headers={'X-Auth-Token': token}).json()['data']
            descriptions = [i['description'] for i in posts_info]
        except KeyError:
            logging.exception('Invalid data in requests')

        if len(descriptions) > 0:
            logging.info('Success')
        else:
            logging.info('Failed to create post!')

        return descriptions
