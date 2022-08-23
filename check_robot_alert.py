from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))        


try:
        link = "http://suninjuly.github.io/alert_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        alert = browser.switch_to.alert
        alert.accept()

        element_x = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
        x = element_x.text
        y = calc(x)

        input1 = browser.find_element(By.CSS_SELECTOR, "#answer.form-control")
        input1.send_keys(y)

        button1 = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
        button1.click()

finally:
        time.sleep(10)
        browser.quite()


