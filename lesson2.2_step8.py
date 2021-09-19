import time
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

with open("file.txt", "w") as file:
    content = file.write("Tanyuhich")
    
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_name('email')
    input3.send_keys("tati.dmi@mail.ru")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.getcwd() + '/' + file.name
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
    element.send_keys(path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла