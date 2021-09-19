from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from send_answer import send_answer
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "https://stepik.org/lesson/181384/step/8"
  
try:  
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
        
    button2 = browser.find_element_by_id('solve')
    button2.click()
    
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    answer = alert_text.split(': ')[-1]
    
    # успеваем скопировать код за 30 секунд
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()

finally:
    send_answer(answer, link)
    time.sleep(5)
    browser.quit()