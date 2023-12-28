import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.primevideo.com/")
act=ActionChains(d)
cat=d.find_element(By.XPATH,'//ol[@class="q06JUe"]//li[3]//label//a')
act.move_to_element(cat).perform()
sub_cat=d.find_element(By.XPATH,'//*[@id="pv-nav-container"]/div/div[1]/div/ol/li[3]/div/div[1]/ul/li[7]/a')


act.move_to_element(sub_cat).click().perform()
time.sleep(3)
d.quit()