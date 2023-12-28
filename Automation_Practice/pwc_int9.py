import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d=webdriver.Chrome()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
drpdwn=Select(d.find_element(By.ID,"RESULT_RadioButton-3"))
drpdwn.select_by_visible_text("Automation Engineer")
time.sleep(5)