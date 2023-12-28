import time

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.get("https://itera-qa.azurewebsites.net/home/automation")
d.find_element(By.ID,"name").send_keys("Utsav")
d.find_element(By.ID,"phone").send_keys("123456789")
d.find_element(By.ID,"email").send_keys("abcd@efgs.com")
d.find_element(By.XPATH,"//input[@id='male']").click()
day=d.find_elements(By.XPATH,"//input[contains(@id,'day')]")
for j in day:
    j.click()

d.find_element(By.XPATH,'//label[@class="custom-control-label" and contains(text(),"4 years") ]').click()
tool=["Testing Webdriver","TestNG","Testim"]
tools=d.find_elements(By.XPATH,'//label[@class="custom-control-label"]')

for i in tools:
    k=i.text
    if k in tool:
        i.click()
time.sleep(5)
d.quit()