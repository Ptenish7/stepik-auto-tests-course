import time
import math
from selenium import webdriver
from send_answer import send_answer

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'https://stepik.org/lesson/184253/step/6?unit=158843'
      
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_css_selector("button.trollface")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()
    answer = alert_text.split(': ')[-1]
    
    time.sleep(1)
    browser.quit()

finally:
    send_answer(answer, link)
    time.sleep(5)
    browser.quit()