import time

from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://jqueryui.com/datepicker/")
d.switch_to.frame(0)
d.find_element(By.CLASS_NAME,"hasDatepicker").click()
year=int(2024)
Month="February"
Date=13

while True:
    mon = d.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    yr = int(d.find_element(By.CLASS_NAME, "ui-datepicker-year").text)
    if mon==Month and yr==year:
        break;
    else:
        d.find_element(By.XPATH,"//span[contains(text(),'Next')]").click()

for r in range(2, 6):
    for c in range(1, 8):
        dat =d.find_element(By.XPATH,'//table[@class="ui-datepicker-calendar"]//tbody//tr[' + str(r) + ']//td[' + str(c) + ']').text
        if dat == Date:
            d.find_element(By.XPATH,'//table[@class="ui-datepicker-calendar"]//tbody//tr[' + str(r) + ']//td[' + str(c) + ']').click()
            break;
time.sleep(3)