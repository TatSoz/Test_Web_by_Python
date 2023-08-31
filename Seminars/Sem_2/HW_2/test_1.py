import yaml
import time
from module import Site

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


sleep = testdata['sleep_time']
site = Site(testdata['address'])
name = testdata['username']
passwd = testdata['password']
post_title = testdata['post_title']
post_descr = testdata['post_descr']
post_content = testdata['post_content']

def test_step1(x_selector_1, x_selector_2, btn_selector_1, x_selector_3, expected_result_1):
    input1 = site.find_element('xpath', x_selector_1)
    input1.send_keys('test')
    input2 = site.find_element('xpath', x_selector_2)
    input2.send_keys('test')
    btn = site.find_element('css', btn_selector_1)
    btn.click()
    err_label = site.find_element('xpath', x_selector_3)
    result = err_label.text
    assert result == expected_result_1, 'Test1 Fail'



def test_entrance(x_selector_1, x_selector_2, btn_selector_1, expected_result_1, x_selector_4, expected_result_2):
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(name)
    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(passwd)
    btn = site.find_element('css', btn_selector_1)
    btn.click()
    link1 = site.find_element('xpath', x_selector_4)
    result = link1.text
    assert result == expected_result_2, 'Test_entrance Fail'



def test_add_post(btn_selector_2, btn_selector_3,
                  x_selector_5, x_selector_6, x_selector_7, x_selector_8):

    btn = site.find_element('xpath', btn_selector_2)
    btn.click()

    input1 = site.find_element('xpath', x_selector_5)
    input1.send_keys(post_title)

    input2 = site.find_element('xpath', x_selector_6)
    input2.send_keys(post_descr)

    input3 = site.find_element('xpath', x_selector_7)
    input3.send_keys(post_content)

    save_btn = site.find_element('xpath', btn_selector_3)
    save_btn.click()

    time.sleep(sleep)
    post_name = site.find_element('xpath', x_selector_8).text

    site.close()

    assert post_name == post_title, 'Test 3 failed'