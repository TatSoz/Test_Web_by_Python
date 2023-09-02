from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """Класс, содержащий необходимые методы для работы с webdriver"""
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'

    def find_element(self, locator, time=10):
        """Метод, осуществляющий поиск одного элемента и возвращающий его"""
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def get_element_property(self, locator, el_property):
        """Метод, возвращающий свойство одного элемента"""
        element = self.find_element(locator)
        return element.value_of_css_property(el_property)

    def go_to_site(self):
        """Переход на указанную страницу"""
        return self.driver.get(self.base_url)