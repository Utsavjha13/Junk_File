from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
for r in range(2,8):
    l=d.find_element(By.XPATH,'//*[@name="BookTable"]//tbody//tr[' +str(r)+']//td[4]')
    if int(l.text) >= 1000:
        book_name= l=d.find_element(By.XPATH,'//*[@name="BookTable"]//tbody//tr[' +str(r)+']//td[1]')
        print(book_name.text)

    