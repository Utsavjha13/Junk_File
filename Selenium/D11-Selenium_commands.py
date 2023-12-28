# Wait Command explicit wait command.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d=webdriver.Chrome()
d.maximize_window()
mywait=WebDriverWait(d,10)
d.get("https://www.google.com/")
search=d.find_element(By.NAME,"q")
search.send_keys("Prime Video")
search.submit()
searchLink= mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='tads']/div/div/div/div/div[1]/a/div[1]/span")))
searchLink.click()
d.quit()
