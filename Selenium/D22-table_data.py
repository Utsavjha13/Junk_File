import time

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
colm=len(d.find_elements(By.XPATH,'//table[@name="BookTable"]//tbody//tr[1]//th'))
row=len(d.find_elements(By.XPATH,'//table[@name="BookTable"]//tbody//tr'))
print("No. of column is :", colm)
print("No. of row is :",row)
print("=========================================================================================")
for i in range (2,row+1):
    for j in range (1,colm+1):
        datas=d.find_element(By.XPATH,'//table[@name="BookTable"]//tbody//tr['+str(i)+']//td['+str(j)+']')
        print(datas.text,end="    ")

    print("")

print("=========================================================================================")
for i in range (2, row+1):
    data=d.find_element(By.XPATH,'//table[@name="BookTable"]//tbody//tr['+str(i)+']//td[2]')
    if data.text=="Mukesh":
        book=d.find_element(By.XPATH,'//table[@name="BookTable"]//tbody//tr['+str(i)+']//td[1]')
        price=d.find_element(By.XPATH,'//table[@name="BookTable"]//tbody//tr['+str(i)+']//td[4]')
        print(book.text," is written by", data.text, "and price is ",price.text)
d.quit()