import time

# Browser commands close and quit

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
d.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
d.close()
time.sleep(5)
d.quit()