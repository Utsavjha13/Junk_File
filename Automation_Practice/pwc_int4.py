import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
d.implicitly_wait(10)
cont=Select(d.find_element(By.ID,"country"))
cont.select_by_value("india")
color=Select(d.find_element(By.ID,"colors"))
color.select_by_value("red")
color.select_by_value("green")
time.sleep(3)