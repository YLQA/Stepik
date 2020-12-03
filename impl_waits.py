from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    button = browser.find_element_by_id('book').click()
    x_val = browser.find_element_by_id('input_value').text
    y = calc(int(x_val))
    scroll = browser.execute_script("window.scrollBy(0, 100);")
    field = browser.find_element_by_id('answer').send_keys(y)
    sub = browser.find_element_by_id('solve').click()

finally:
    # успеваем скопировать код за 30 секунд
    #time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()