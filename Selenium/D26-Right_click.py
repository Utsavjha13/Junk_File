import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button=d.find_element(By.XPATH,"//*[@class='context-menu-one btn btn-neutral']")
act=ActionChains(d)
act.context_click(button).perform()
time.sleep(3)
d.find_element(By.XPATH,"/html/body/ul/li[5]").click()
time.sleep(2)
promt=d.switch_to.alert
promt.accept()
time.sleep(2)
d.quit()