# Wait Command Implicit wait command.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.google.com/")
d.refresh()
search=d.find_element(By.NAME,"q")
search.send_keys("Prime Video")
search.submit()
pv=d.find_element(By.XPATH,"//*[@id='tads']/div/div/div/div/div[1]/a/div[2]/span[1]/span[2]/span[2]/span")
# pv=d.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a/div/div/span")
pv.click()
d.find_element(By.XPATH,"//*[@id='pv-nav-container']/div/div[2]/div[1]/input").click()
srch_pv=d.find_element(By.XPATH,"//*[@id='pv-search-nav']")
srch_pv.send_keys("bhola")
srch_pv.submit()
result=d.find_elements(By.XPATH,"//article[@class='Z9dd1d']")
print("total search result: ",len(result))
d.quit()