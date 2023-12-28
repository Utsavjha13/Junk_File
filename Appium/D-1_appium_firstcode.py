from appium import webdriver
import unittest

from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

desired_cap={
  "appium:automationName": "UIAutomator2",
  "platformName": "Android",
  "appium:appPackage": "com.sling",
  "appium:appActivity": "com.sling.MainActivity"
}
appium_s="http://0.0.0.0:4723/wd/hub"
# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(desired_cap)
driver=webdriver.Remote(appium_s,options=capabilities_options)
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup").click()
driver.find_element(By.XPATH,"//*[@text='SIGN IN']").click()
driver.find_element(By.XPATH,'//android.widget.EditText[@content-desc="Email Address"]').send_keys("atpauto19@sling.com")
driver.find_element(By.XPATH,'//android.widget.EditText[@content-desc="Password"]').send_keys("Watchm3")
driver.find_element(By.XPATH,'//*[contains(@text,"SIGN IN")]').click()