import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc1(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def test_1():
    chrome = webdriver.Chrome('./chromedriver.exe')
    chrome.implicitly_wait(15)
    chrome.get('http://suninjuly.github.io/explicit_wait2.html')
    chrome.maximize_window()

    try:
        price = WebDriverWait(chrome, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '100'))
        chrome.find_element(By.ID, 'book').click()
        x =chrome.find_element(By.ID, 'input_value').text
        y = calc1(x)
        chrome.find_element(By.ID, 'answer').send_keys(y)
        chrome.find_element(By.ID, 'solve').click()

        chrome.switch_to.alert
    finally:
        time.sleep(4)
        chrome.quit()
