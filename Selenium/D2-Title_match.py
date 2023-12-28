from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver= wd.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.NAME,"Email").clear()
driver.find_element(By.NAME,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.NAME, "Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
driver.find_element(By.CLASS_NAME,"login-button").click()
title=driver.title
expected= "Dashboard / nopCommerce administration"
if title==expected:
    print("title matched")
else:
    print("Title not matched")