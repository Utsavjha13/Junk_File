import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
drg=d.find_element(By.ID, "draggable")
drp=d.find_element(By.ID,"droppable")
act=ActionChains(d)
act.drag_and_drop(drg,drp).perform()
time.sleep(5)