import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.geeksforgeeks.org/interview-preparation-for-software-developer/")

# focus will be on 1st tab only
d.find_element(By.XPATH,'//*[@id="hslider"]/li[8]/a').send_keys(Keys.COMMAND+Keys.ENTER)

d.switch_to.new_window("tab") #will open new tab focus will be on new tab
d.get("https://testautomationpractice.blogspot.com/")

d.switch_to.new_window("window")#will open new Window focus will be on new Window
d.get("https://demo.automationtesting.in/Register.html")
time.sleep(3)
d.quit()