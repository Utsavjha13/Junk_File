from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import options
import time

# serv_obj = Service("Mojava/Users/utsav.jha/Downloads/chromedriver_mac64/chromedriver")
# driver = webdriver.Chrome(service=serv_obj)
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com")
time.sleep(5)
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

title=driver.title
expt_title="OrangeHRM"
if title==expt_title:
    print("login test pass")
else:
    print("failed")