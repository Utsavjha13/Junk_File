import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
d.find_element(By.NAME, "username").send_keys("Admin")
d.find_element(By.NAME, "password").send_keys("admin123")
d.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
act=ActionChains(d)
cat=d.find_element(By.XPATH,'//*[@class="oxd-topbar-body"]//nav//ul//li[4]//span')
act.move_to_element(cat).click().perform()
subCat=d.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]/a')
act.move_to_element(subCat).click().perform()
time.sleep(5)