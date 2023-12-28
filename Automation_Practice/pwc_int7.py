import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
d.implicitly_wait(10)
d.find_element(By.XPATH,"//button[normalize-space()='Alert']").click()
d.switch_to.alert.accept()
d.find_element(By.XPATH,"//button[normalize-space()='Confirm Box']").click()
d.switch_to.alert.dismiss()
d.find_element(By.XPATH,"//button[normalize-space()='Prompt']").click()
alrt=d.switch_to.alert
alrt.send_keys("Utsav Jha")
alrt.accept()
time.sleep(3)