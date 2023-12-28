import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(3)