from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://github.com/login")
time.sleep(1)
driver.find_element_by_id("login_field").send_keys("email/username")
time.sleep(1)
driver.find_element_by_id("password").send_keys("password")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/main/div/div[4]/form/div/input[12]").click()
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/summary/span[2]").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/header/div[7]/details/details-menu/form/button").click()
time.sleep(5)
driver.close()
print ("Failed login and log out")