import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.primevideo.com/")
d.find_element(By.XPATH,"//*[@id='pv-nav-container']/div/div[1]/div/ol/li[3]/div/div[1]/ul/li[7]/a").click()
ele=d.find_elements(By.XPATH,"//li[@class='tHfREs']")
print("No of movies: ",len(ele))
for i in ele:
    print(i.text)
