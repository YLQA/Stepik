from selenium import webdriver
import time
import math

link = " http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
browser.get(link)
try:
    picture = browser.find_element_by_id('treasure')
    val = picture.get_attribute("valuex")
    y = calc(val)
    select = Select(browser.find_element_by_tag_name("select"))
    sub = browser.find_element_by_class_name('btn.btn-default').click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()