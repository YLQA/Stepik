import os
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser.get(link)
    start = browser.find_element_by_class_name('btn.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x_val = browser.find_element_by_id('input_value').text
    y = calc(int(x_val))
    enter_field = browser.find_element_by_id('answer').send_keys(y)
    sub = browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()