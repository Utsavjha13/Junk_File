import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://the-internet.herokuapp.com/javascript_alerts")
d.find_element(By.XPATH,"//*[@class='example']//ul//li[3]//button").click()
promt=d.switch_to.alert
promt.send_keys("Utsav")
promt.accept()
time.sleep(3)
d.find_element(By.XPATH,"//*[@class='example']//ul//li[2]//button").click()
d.switch_to.alert.dismiss()

time.sleep(3)
d.quit()
