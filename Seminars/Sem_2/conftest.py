import pytest
import yaml

with open('testdata.yaml') as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_selector_1():
    return 'button'


@pytest.fixture()
def expected_result_1():
    return '401'


@pytest.fixture()
def x_selector_4():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'


@pytest.fixture()
def expected_result_2():
    return f'Hello, {testdata["username"]}'