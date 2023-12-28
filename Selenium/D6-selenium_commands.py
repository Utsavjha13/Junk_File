# Conditional command is_displayed, is_enabled, is_selected
from selenium import webdriver
from selenium.webdriver.common.by import By
d=webdriver.Chrome()
d.get("https://www.primevideo.com/")
catg=d.find_element(By.XPATH, "//*[@id='pv-nav-container']/div/div[1]/div/ol/li[3]/label/a")
print("Displayed:",catg.is_displayed())
print("Enabled:",catg.is_enabled())
print("Selected:",catg.is_selected())
d.quit()