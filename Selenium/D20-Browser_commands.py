import time

import action as action
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
d.find_element(By.CLASS_NAME,"wikipedia-search-input").send_keys("Selenium")
d.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
d.find_element(By.XPATH,"//*[@class='wikipedia-search-results']//div[1]/a").click()
d.find_element(By.XPATH,"//*[@class='wikipedia-search-results']//div[2]/a").click()
d.find_element(By.XPATH,"//*[@class='wikipedia-search-results']//div[3]/a").click()
d.find_element(By.XPATH,"//*[@class='wikipedia-search-results']//div[4]/a").click()
d.find_element(By.XPATH,"//*[@class='wikipedia-search-results']//div[5]/a").click()
winID=d.window_handles
for i in winID:
    d.switch_to.window(i)
    print(d.title)
for j in winID:
    d.switch_to.window(j)
    if d.title=="Selenium in biology - Wikipedia" or d.title=="Selenium disulfide - Wikipedia":
        print("window closed :", d.title)
        d.close()
d.quit()

