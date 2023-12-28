import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://gotranscript.com/text-compare")
input1=d.find_element(By.NAME,'text1')
input2=d.find_element(By.NAME,'text2')
# d.find_element(By.XPATH,'//*[@class="close-icon_circle__l09BK"]').click()
input1.send_keys("I am learning selenium")

act=ActionChains(d)
act.key_down(Keys.COMMAND).send_keys("a").perform()
act.key_up(Keys.COMMAND).perform()

act.key_down(Keys.COMMAND).send_keys("c").perform()
act.key_up(Keys.COMMAND).perform()

act.key_down(Keys.TAB).perform()
act.key_up(Keys.TAB)
act.perform()

act.key_down(Keys.COMMAND).send_keys("v").perform()
act.key_up(Keys.COMMAND).perform()
time.sleep(3)