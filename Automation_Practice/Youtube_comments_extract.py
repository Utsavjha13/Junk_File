import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

yd=webdriver.Chrome()
yd.maximize_window()
yd.implicitly_wait(10)
mywait=WebDriverWait(yd,10)
yd.get("https://www.youtube.com/")
searchbox=yd.find_element(By.XPATH,"//*[@name='search_query']")
searchbox.send_keys("Hanuman chalisa")
searchbox.submit()
yd.find_element(By.XPATH,"//*[@class='style-scope ytd-section-list-renderer']//div[3]//ytd-video-renderer[1]").click()
comments=yd.find_elements(By.XPATH,'//yt-formatted-string[@id="content-text"]//span')
for i in comments:
    print(i)
time.sleep(5)