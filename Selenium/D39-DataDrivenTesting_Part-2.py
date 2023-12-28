from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import xLUtility
import time
d=webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
cookies=d.find_element(By.ID,'wzrk-cancel')
cookies.click()
file="/Users/utsav.jha/Downloads/moneyControl.xlsx"
c=xLUtility.get_max_col(file,"Sheet1")
r=xLUtility.get_max_row(file,"Sheet1")
for i in range(2,r+1):
    prins=xLUtility.read_data(file,"Sheet1",i,1)
    d.find_element(By.ID,"principal").send_keys(prins)
    intrst=xLUtility.read_data(file,"Sheet1",i,2)
    d.find_element(By.ID,"interest").send_keys(intrst)
    tenure = xLUtility.read_data(file, "Sheet1", i, 3)
    d.find_element(By.ID, "tenure").send_keys(tenure)
    tenurePeriod = xLUtility.read_data(file, "Sheet1", i, 4)
    tp=Select(d.find_element(By.ID, "tenurePeriod"))
    tp.select_by_visible_text(tenurePeriod)
    freq= xLUtility.read_data(file, "Sheet1", i, 5)
    freqs=Select(d.find_element(By.ID,"frequency"))
    freqs.select_by_visible_text(freq)
    calculate=d.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]')
    calculate.click()
    maturT=d.find_element(By.XPATH,'//*[@id="resp_matval"]')
    maturity=xLUtility.write_data(file, "Sheet1", i, 6,float(maturT.text))
    expected=xLUtility.write_data(file, "Sheet1", i, 7,"Passed")
    expectedfill=xLUtility.green_color_cell(file, "Sheet1", i, 7)
    d.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]').click()

