from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

d=webdriver.Chrome()
d.get("https://testautomationpractice.blogspot.com/")
d.maximize_window()
d.implicitly_wait(10)
d.find_element(By.CLASS_NAME, "hasDatepicker").click()
mon="February"
y=1993
D="13"
while True:
    month=d.find_element(By.CLASS_NAME,"ui-datepicker-month").text
    year=d.find_element(By.CLASS_NAME,"ui-datepicker-year").text
    if  (int(year)==y and mon==month):
        break
    elif y<int(year):
        d.find_element(By.XPATH,"//a[contains(@title,'Prev')]").click()
    elif y==int(year) and mon!=month:
        d.find_element(By.XPATH,"//a[contains(@title,'Prev')]").click()

for r in range(2,8):
    for c in range(1,8):
        date=d.find_element(By.XPATH,"//table[@class='ui-datepicker-calendar']//tbody//tr[" + str(r) +"]//td["+str(c)+"]")
        if D==date.text:
            date.click()
            break




