import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
d.switch_to.default_content()
d.switch_to.frame("frame-one796456169")
d.find_element(By.ID,"RESULT_TextField-0").send_keys("Utsav Jha")
d.find_element(By.XPATH,'//input[@id="RESULT_RadioButton-1_0"]').click()
time.sleep(3)