import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# scroll down the page by pixel
d.execute_script("window.scrollBy(0,3000)","") #this java script need to remember for scroll till pixel number mentioned
value=d.execute_script("return window.pageYOffset;")#this java script need to remember for finding current pixel
print("pixel :",value)
time.sleep(2)

# scroll down till find element
flag=d.find_element(By.XPATH,'//img[@alt="Flag of India"]')
d.execute_script("arguments[0].scrollIntoView();",flag)
value=d.execute_script("return window.pageYOffset;")
print("india :",value)
time.sleep(2)

# Scroll down till end
d.execute_script("window.scrollBy(0,document.body.scrollHeight)") #this java script need to remember for scroll till end
value=d.execute_script("return window.pageYOffset;")#this java script need to remember for finding current pixel
print("pixel end:",value)
time.sleep(2)
#scroll up till start
d.execute_script("window.scrollBy(0,-document.body.scrollHeight)") #this java script need to remember for scroll till end
value=d.execute_script("return window.pageYOffset;")#this java script need to remember for finding current pixel
print("pixel start:",value)
time.sleep(2)