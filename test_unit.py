from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
import math

list_of_subpages = ['236895', '236896', '236897',
                    '236898', '236899', '236903',
                    '236904', '236905']


def get_time_fun():
    return math.log(int(time.time()))


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.mark.parametrize('page_num', list_of_subpages)
def test_solving_task(browser, page_num):
    link = "https://stepik.org/lesson/{}/step/1".format(page_num)
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.textarea').send_keys(str(get_time_fun()))
    browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
    hint_message = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    assert hint_message == 'Correct!', 'Fail in test on page {}'.format(link)
