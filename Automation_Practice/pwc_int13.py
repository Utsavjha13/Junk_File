import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
d.implicitly_wait(10)
d.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("Good")
d.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
d.find_element(By.ID,"Wikipedia1_wikipedia-search-more").click()
d.switch_to.new_window('tab')
time.sleep(5)
l=d.window_handles
d.switch_to.window(l[0])
time.sleep(3)