import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://demo.automationtesting.in/Register.html")
# d.execute_script("window.scrollBy(0,document.body.scrollHeight)")
d.find_element(By.XPATH,'//*[@id="imagesrc"]').send_keys("/Users/utsav.jha/Downloads/screenshot&Videos/file-sample_100kB.doc")
time.sleep(4)