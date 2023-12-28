import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
ele=WebDriverWait(d,10,ElementNotInteractableException).until(EC.element_to_be_clickable((By.XPATH,"//th[normalize-space()='BookName']")))
time.sleep(10)  