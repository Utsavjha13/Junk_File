import time

import action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
d.implicitly_wait(10)
dblclk=d.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act=ActionChains(d)
act.double_click(dblclk).perform()
time.sleep(5)