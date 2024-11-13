import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开A页面, 输入用户名 admin, 暂停3s, 双击鼠标左键(选中admin)
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
element = driver.find_element(By.ID,"userA")
element.send_keys("admin")
time.sleep(3)
driver.maximize_window()
action = ActionChains(driver)
action.double_click(element).perform()

time.sleep(7)
driver.quit()
