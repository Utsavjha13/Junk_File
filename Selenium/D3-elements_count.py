from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.geeksforgeeks.org/how-to-automate-amazon-like-e-commerce-website-with-selenium/")
slider=driver.find_elements(By.CLASS_NAME, "header-main__slider")
print(len(slider))
tagname=driver.find_elements(By.TAG_NAME,"a")
print(len(tagname))