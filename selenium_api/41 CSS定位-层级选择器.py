import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开A页面, 使用CSS定位方式中的层级选择器, 定位用户名输入框, 并输入 admin
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
# driver.find_element(By.CSS_SELECTOR,"p[id='pa']>input").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"div[class='zc'] input").send_keys("admin")

time.sleep(5)
driver.close()