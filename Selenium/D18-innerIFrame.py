import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://demo.automationtesting.in/Frames.html")
d.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
outerframe=d.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
d.switch_to.frame(outerframe)
innerframe=d.find_element(By.XPATH,"/html/body/section/div/div/iframe")
d.switch_to.frame(innerframe)
d.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("frame is done!")
time.sleep(3)
d.quit()
