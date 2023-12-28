import time

from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
d.switch_to.frame("packageListFrame")
d.find_element(By.LINK_TEXT,"org.openqa.selenium.chromium").click()

d.switch_to.default_content()
d.switch_to.frame("packageFrame")
d.find_element(By.LINK_TEXT,"ChromiumDriver").click()

d.switch_to.default_content()
d.switch_to.frame("classFrame")
d.find_element(By.LINK_TEXT,"EdgeDriver").click()
time.sleep(5)
d.quit()