import os
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser.get(link)
    start = browser.find_element_by_class_name('trollface.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    start_new_window = browser.switch_to.window(new_window)
    x_val = browser.find_element_by_id('input_value').text
    y = calc(int(x_val))
    enter_field = browser.find_element_by_id('answer').send_keys(y)
    sub = browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()