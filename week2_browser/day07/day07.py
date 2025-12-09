from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import service
from selenium.webdriver.common.by import By
import time
def fill_username(driver, username):
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys(username)

service = Service("chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/login")
driver.implicitly_wait(10)

fill_username(driver, "tomsmith")
time.sleep(5)
driver.quit()
