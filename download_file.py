import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
first_name = 'Yevhen'
last_name = 'Grand'
email = 'test@test.org'
try:
    browser.get(link)
    first_field = browser.find_element_by_name("firstname").send_keys(first_name)
    second_field = browser.find_element_by_name("lastname").send_keys(last_name)
    third_field = browser.find_element_by_name("email").send_keys(email)
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    sent_file = browser.find_element_by_id("file").send_keys(file_path)
    sub = browser.find_element_by_class_name("btn.btn-primary").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()