import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"male").click()
l=driver.find_elements(By.XPATH,'//input[contains(@id,"day")]')
for i in l:
    if i.get_attribute("id") in ("sunday","monday","friday"):
        i.click()


time.sleep(3)