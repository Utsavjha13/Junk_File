import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
d=webdriver.Chrome()
d.maximize_window()
d.get("https://www.primevideo.com/")
d.find_element(By.XPATH,"/html/body/div[1]/div[1]/header/div[1]/div/div/div/div[2]/div[1]/input").click()
time.sleep(5)
d.find_element(By.XPATH,"//*[@id='pv-search-nav']").send_keys("Bhola")
d.find_element(By.XPATH,"//*[@id='pv-search-nav']").send_keys(Keys.ENTER)
print(d.title)