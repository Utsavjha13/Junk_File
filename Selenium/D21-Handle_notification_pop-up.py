import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# for disabling notification.
ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

d=webdriver.Chrome(options=ops)
d.maximize_window()
d.get("https://www.gps-coordinates.net/my-location")
time.sleep(15)