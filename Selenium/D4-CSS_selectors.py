from selenium import webdriver
from selenium.webdriver.common.by import By
import time
d= webdriver.Chrome()
d.maximize_window()
d.get("https://www.primevideo.com/")
d.find_element(By.CSS_SELECTOR,"button.DVPAWebWidgetsUI_Button__button").click()
d.find_element(By.CSS_SELECTOR,"input#ap_email").clear()
d.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("utsav.jha@dish.com")
d.find_element(By.CSS_SELECTOR,"input.a-input-text[name='password']").clear()
d.find_element(By.CSS_SELECTOR,"input.a-input-text[name='password']").send_keys("Sling@321")
d.find_element(By.CSS_SELECTOR,"#signInSubmit").click()
time.sleep(10)
titled=d.title
print(titled)