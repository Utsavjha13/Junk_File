import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
act=ActionChains(d)
slider=d.find_element(By.XPATH,'//*[@class="ui-slider-handle ui-corner-all ui-state-default"]')
print("before :",slider.location)
act.drag_and_drop_by_offset(slider,250,0).perform()
print("After :",slider.location)
time.sleep(2)
d.quit()