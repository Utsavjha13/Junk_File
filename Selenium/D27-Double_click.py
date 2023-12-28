import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
button=d.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
act=ActionChains(d)
act.double_click(button).perform()
time.sleep(3)
d.quit()