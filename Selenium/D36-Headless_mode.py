import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
ops=webdriver.ChromeOptions()
ops.add_argument("--headless")
d=webdriver.Chrome(options=ops)
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.geeksforgeeks.org/interview-preparation-for-software-developer/")
print(d.title)
print(d.current_url)
d.quit()