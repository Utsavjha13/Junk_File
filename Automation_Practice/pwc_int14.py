import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
d.find_element(By.CLASS_NAME,"widget-content").click()
d.switch_to.new_window("tab")
time.sleep(3)
d.close()
