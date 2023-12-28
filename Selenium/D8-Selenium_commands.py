# Navigational command back, forward, refresh
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.get("https://www.primevideo.com/")
d.get("https://www.orangehrm.com/")
time.sleep(2)
d.back()
time.sleep(2)
d.forward()
time.sleep(2)
d.refresh()
time.sleep(2)
d.quit()