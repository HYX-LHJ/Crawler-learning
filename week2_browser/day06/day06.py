from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

# 1. 指定 chromedriver 的路径
service = Service("chromedriver.exe")

# 2. 创建浏览器对象
driver = webdriver.Chrome(service=service)

# 3. 打开一个网页
driver.get("https://www.google.com")
print(driver.current_url)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("google_home.png")



# 4. 停留 5 秒，让你看到浏览器打开成功
time.sleep(5)

# 5. 关闭浏览器
driver.quit()
