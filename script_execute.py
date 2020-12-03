from selenium import webdriver
import time
import math

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser.get(link)
try:
    x_val = browser.find_element_by_id('input_value').text
    y = calc(int(x_val))
    scroll = browser.execute_script("window.scrollBy(0, 100);")
    field = browser.find_element_by_id('answer').send_keys(y)
    check = browser.find_element_by_css_selector("[for='robotCheckbox']").click()
    radio = browser.find_element_by_css_selector("[for='robotsRule']").click()
    sub = browser.find_element_by_class_name('btn.btn-primary').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
