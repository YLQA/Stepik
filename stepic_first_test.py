from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"
browser = webdriver.Chrome()




try:

    # browser.get(link)
    # elements = browser.find_elements_by_xpath("form/div/input[@type='text']")
    # for element in elements:
    #     element.send_keys("Мой ответ")
    #
    # button = browser.find_element_by_css_selector("button.btn")
    # button.click()
    browser.get(link)
   


    input1 = browser.find_element_by_name("first_name").send_keys("Ivan")

    input2 = browser.find_element_by_name("last_name").send_keys("Petrov")

    input3 = browser.find_element_by_class_name("form-control.city").send_keys("Smolensk")

    input4 = browser.find_element_by_id("country").send_keys("Russia")

    button = browser.find_element_by_xpath('//button[text()="Submit"]').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
