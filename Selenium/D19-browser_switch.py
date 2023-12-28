import time

import action as action
from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# WD=WebDriverWait(d,10)
# dclik=WD.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[1]/div[2]/div[4]/div[2]/a")))
# actions.doubleClick(dclik).perform()
d.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
winID= d.window_handles
# Approch 1
# d.switch_to.window(winID[0])
# print(d.title)
# d.switch_to.window(winID[1])
# print(d.title)

# Approch 2
time.sleep(3)
for i in winID:
    d.switch_to.window(i)
    print(d.title)
    if d.title=="OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        d.close()