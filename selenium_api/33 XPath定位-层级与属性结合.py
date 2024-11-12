import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 打开A页面完成以下操作
# 使用层级与属性结合的定位策略, 在test1对应的输入框里输入: test1
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

driver.find_element(By.XPATH,"//*[@id='p1']/input").send_keys("test1")

time.sleep(5)
driver.close()