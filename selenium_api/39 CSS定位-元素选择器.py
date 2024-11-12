import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开A页面, 使用CSS定位方式中的元素选择器, 定位注册按钮, 并点击
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
driver.find_element(By.CSS_SELECTOR,"button").click()

time.sleep(5)
driver.close()