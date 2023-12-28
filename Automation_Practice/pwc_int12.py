import time

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")


for r in range(1,5):
    l=(d.find_element(By.XPATH,'//*[@id="productTable"]//tbody//tr['+str(r)+']//td[3]')).text
    price=l.lstrip("$")
    if float(price)>=10:
        d.find_element(By.XPATH, '//*[@id="productTable"]//tbody//tr[' + str(r) + ']//td[4]//input[@type="checkbox"]').click()
time.sleep(5)