import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

# 八中定位方法都适用"另一种方法"
# driver.find_element(By.ID, "userA").send_keys("admin")
driver.find_element(By.XPATH, "//*[@placeholder='请输入电子邮箱']").send_keys("123456@qq.com")

time.sleep(5)
driver.close()