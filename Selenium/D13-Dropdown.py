import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://itera-qa.azurewebsites.net/home/automation")
dropD=Select(d.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div/select'))
dropD.select_by_visible_text("Greece")
all_value=dropD.options

print("all value in dropdown: ", len(all_value))
for i in all_value:
    print(i.text)

time.sleep(2)
d.quit()