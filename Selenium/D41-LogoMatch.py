import time
import PIL
from PIL import Image, ImageChops, ImageStat
from selenium import webdriver
from selenium.webdriver.common.by import By


output_logo = "/Users/utsav.jha/PycharmProjects/Testing/Selenium/original.png"
input_logo = "/Users/utsav.jha/PycharmProjects/Testing/Selenium/actual.png"
d = webdriver.Chrome()
d.maximize_window()
d.implicitly_wait(10)
d.get("https://demo.automationtesting.in/Register.html")
with open(output_logo, 'wb') as file:
    file.write(d.find_element(By.XPATH, '//img[@id="imagetrgt"]').screenshot_as_png)
    img1 = PIL.Image.open(input_logo)
    img2 = PIL.Image.open(output_logo)
    logoresult = ImageChops.difference(img1, img2)
    stat = ImageStat.Stat(logoresult)
    diff = sum(stat.mean)
    print(diff)

    if diff > 0:
        print('Not Matched')
    else:
        print("Matched")
