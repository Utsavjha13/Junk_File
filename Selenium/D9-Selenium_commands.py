import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
d=webdriver.Chrome()
d.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Feu.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3Dsg8QIBys6XmdzMEOrUlBDzV3pccAXkkNBqh0TzqKqfp8HAAAAAQAAAABkbjo-cmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Foffers%2Fnonprimehomepage%3Fref_%253Datv_hm_Categories_c_9zZ8D2_1_0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=amzn_prime_video_sso_in&openid.mode=checkid_setup&siteState=258-6663630-6002545&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
time.sleep(2)
ele=d.find_element(By.XPATH,"//*[@id='ap_email']")
ele.send_keys("utsav.jha@dish.com")
print(ele.get_attribute("value"))
print(ele.get_attribute("name"))
print(ele.get_attribute("id"))
d.quit()