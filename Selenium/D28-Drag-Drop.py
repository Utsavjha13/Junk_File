import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

act=ActionChains(d)
wc_source=d.find_element(By.ID,"box3")
wc_target=d.find_element(By.ID,"box103")
act.drag_and_drop(wc_source,wc_target).perform()
oslo_source=d.find_element(By.ID,"box1")
oslo_target=d.find_element(By.ID,"box101")
act.drag_and_drop(oslo_source,oslo_target).perform()
seoul_source=d.find_element(By.ID,"box5")
seoul_target=d.find_element(By.ID,"box105")
act.drag_and_drop(seoul_source,seoul_target).perform()
stoc_source=d.find_element(By.ID,"box2")
stoc_target=d.find_element(By.ID,"box102")
act.drag_and_drop(stoc_source,stoc_target).perform()
rome_source=d.find_element(By.ID,"box6")
rome_target=d.find_element(By.ID,"box106")
act.drag_and_drop(rome_source,rome_target).perform()
mad_source=d.find_element(By.ID,"box7")
mad_target=d.find_element(By.ID,"box107")
act.drag_and_drop(mad_source,mad_target).perform()
cop_source=d.find_element(By.ID,"box4")
cop_target=d.find_element(By.ID,"box104")
act.drag_and_drop(cop_source,cop_target).perform()

time.sleep(3)