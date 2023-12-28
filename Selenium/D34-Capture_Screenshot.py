import time
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.primevideo.com/")
d.save_screenshot("/Users/utsav.jha/Downloads/prime.png")
# d.save_screenshot(os.getcwd()+"prime.png")
# d.get_screenshot_as_png() #it will take screenshot in binary format
# d.get_screenshot_as_base64() #it will take screenshot in binary format