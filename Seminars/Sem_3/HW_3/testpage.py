from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    """Класс для хранения локаторов"""
    # Локатор поля ввода username страницы авторизации
    LOCATOR_LOGIN_FIELD = (By.XPATH, '//*[@id="login"]/div[1]/label/input')
    # Поле ввода password страницы авторизации
    LOCATOR_PASS_FIELD = (By.XPATH, '//*[@id="login"]/div[2]/label/input')
    # Блок ошибки страницы авторизации
    LOCATOR_ERROR_FIELD = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/h2')
    # Ссылка на профиль пользователя с выпадающим меню на главной странице
    LOCATOR_USER_PROFILE_LINK = (By.XPATH, '//*[@id="app"]/main/nav/ul/li[3]/a')
    # Поле ввода Title формы создания поста
    LOCATOR_FORM_POST_TITLE = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[1]/div/label/input')
    # Поле ввода Description формы создания поста
    LOCATOR_FORM_POST_DESCRIPTION = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[2]/div/label/span/textarea')
    # Поле ввода Content формы создания поста
    LOCATOR_FORM_POST_CONTENT = (By.XPATH, '/html/body/div/main/div/div/form/div/div/div[3]/div/label/span/textarea')
    # Название поста на странице поста сразу после его создания
    LOCATOR_POST_NAME = (By.XPATH, '//*[@id="app"]/main/div/div[1]/h1')
    # Кнопка Login страницы авторизации
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, 'button')
    # Кнопка создания поста на главной странице
    LOCATOR_CREATE_POST_BTN = (By.CSS_SELECTOR, '#create-btn')
    # Кнопка сохранения поста SAVE формы создания поста
    LOCATOR_SAVE_POST_BTN = (By.CSS_SELECTOR, '.mdc-button__label')
    # Кнопка "Contact", открытие формы
    LOCATOR_OPEN_FORM_CONTACT_BTN = (By.CSS_SELECTOR, '#app > main > nav > ul > li:nth-child(2) > a')
    # Поле ввода "Your name" в форме обратной связи
    LOCATOR_YOUR_NAME_CONTACT_US = (By.XPATH, '//*[@id="contact"]/div[1]/label/input')
    # Поле ввода " Your email" в форме обратной связи
    LOCATOR_YOUR_EMAIL_CONTACT_US = (By.XPATH, '//*[@id="contact"]/div[2]/label/input')
    # Поле "Content" в форме обратной связи
    LOCATOR_CONTENT_CONTACT_US = (By.XPATH, '//*[@id="contact"]/div[3]/label/span/textarea')
    # Кнопка "CONTACT US" в форме обратной связи
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")
        # (By.CSS_SELECTOR, 'button')





class OperationsHelper(BasePage):
    """Класс, содержащий методы для работы с элементами на веб-страницах"""
    def enter_login(self, word):
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}')
        """Ввод логина username на странице авторизации"""
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        """Ввод пароля password на странице авторизации"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}')
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def get_error_text(self):
        """Ищет элемент с оповещением об ошибке и получает атрибут text"""
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'Founded text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_login_text(self):
        """Возврат имени пользователя"""
        element_successful_login = self.find_element(TestSearchLocators.LOCATOR_USER_PROFILE_LINK, time=2)
        text = element_successful_login.text
        return text

    def get_post_title(self):
        """Возврат названия поста пользователя"""
        element_post_title = self.find_element(TestSearchLocators.LOCATOR_POST_NAME, time=2)
        text = element_post_title.text
        return text

    def enter_post_title(self, word):
        """Ввод заголовка Title в форме создания поста"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_FORM_POST_TITLE[1]}')
        title_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def enter_post_description(self, word):
        """Ввод описания Description в форме создания поста"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_FORM_POST_DESCRIPTION[1]}')
        description_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_DESCRIPTION)
        description_field.clear()
        description_field.send_keys(word)

    def enter_post_content(self, word):
        """Ввод поста Content в форме создания поста"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_FORM_POST_CONTENT[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_FORM_POST_CONTENT)
        content_field.clear()
        content_field.send_keys(word)


    def enter_your_name_contact_us(self, word):
        """Ввод Вашего имени в форме обратной связи"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_YOUR_NAME_CONTACT_US[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_CONTACT_US)
        content_field.clear()
        content_field.send_keys(word)


    def enter_your_mail_contact_us(self, word):
        """ВВод Вашего email в форме обратной связи"""
        logging.info(f'Send {word} to element {TestSearchLocators.LOCATOR_YOUR_EMAIL_CONTACT_US[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_EMAIL_CONTACT_US)
        content_field.clear()
        content_field.send_keys(word)


    def enter_content_contact_us(self, word):
        """ВВод Content в форме обратной связи"""
        logging.info(f'send {word} to element {TestSearchLocators.LOCATOR_CONTENT_CONTACT_US[1]}')
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_CONTACT_US)
        content_field.clear()
        content_field.send_keys(word)



    def click_login_button(self):
        """Нажатие кнопки Login страницы авторизации"""
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def click_create_post_button(self):
        """Нажатие кнопки создания поста"""
        logging.info('Click creating post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN).click()

    def click_save_post_button(self):
        """Нажатие кнопки сохранения поста"""
        logging.info('Click saving post button')
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()


    def click_contact_button(self):
        """Нажатие кнопки Contact, открытие формы"""
        logging.info('Click on the button Contact')
        self.find_element(TestSearchLocators.LOCATOR_OPEN_FORM_CONTACT_BTN).click()


    def click_contact_us_button(self):
        """Клик по кнопке 'CONTACT US' """
        logging.info('Click on the button CONTACT US')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN)


    def get_alert_contact_us(self):
        """Получение текста подстерждение действия на странице """
        logging.info('Get text alert')
        text = self.get_alert_text()
        logging.info(text)
        return text




