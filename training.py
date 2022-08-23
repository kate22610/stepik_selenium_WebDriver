from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
        link = ""
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.CLASS_NAME, "")
        input1.send_keys("")
        input2 = browser.find_element(By.TAG_NAME, "")
        input2.send_keys("")

        button = browser.find_element(By.CSS_SELECTOR, "")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "")
        welcome_text = welcome_text_elt.text

        assert "" == welcome_text

finally:
        time.sleep(10)
        browser.quite()

        
