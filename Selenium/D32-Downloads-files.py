import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

location="/Users/utsav.jha/Downloads/screenshot&Videos"
#   plugins.always_open_pdf_externally should true if pdf is downloading
preferences={"download.default_directory":location,"plugins.always_open_pdf_externally":True}
ops=webdriver.ChromeOptions()
ops.add_experimental_option("prefs",preferences)

d=webdriver.Chrome(options=ops)
d.maximize_window()
d.implicitly_wait(10)
d.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# ele=d.find_element(By.XPATH,'//*[@id="table-files"]/tbody/tr[1]/td[5]/a')
# d.execute_script("arguments[0].scrollIntoView();",ele)
ele2=d.find_element(By.XPATH,'//*[@id="table-files"]/tbody/tr[1]/td[5]/a')
d.execute_script("arguments[0].click();",ele2)
time.sleep(15)
d.quit()