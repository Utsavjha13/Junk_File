from selenium import webdriver
from selenium.webdriver.common.by import By

d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://testautomationpractice.blogspot.com/")
d.find_element(By.CLASS_NAME,"wikipedia-search-input").clear()
d.find_element(By.CLASS_NAME,"wikipedia-search-input").send_keys("adfhsa")
d.find_element(By.CLASS_NAME,"wikipedia-search-button").click()
result=d.find_element(By.ID,"Wikipedia1_wikipedia-search-results")
expected="No results found."
if result==expected:
    assert True
else:
    print("Not matched")