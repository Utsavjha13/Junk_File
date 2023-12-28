import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element(By.ID,"name").send_keys("Utsav")
driver.find_element(By.ID,"email").send_keys("abc@gmail.com")
driver.find_element(By.ID,"phone").send_keys("987654321")
driver.find_element(By.ID,"textarea").send_keys("12,tblock, delhi")
time.sleep(3)
driver.close()