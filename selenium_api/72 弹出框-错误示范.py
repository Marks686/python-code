import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开A页面,完成以下弹出框操作
# 1.点击 alert 按钮
# 2.暂停2s, 输入用户名 admin
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

# 1
driver.find_element(By.ID,"alerta").click()
# 2
time.sleep(2)
driver.find_element(By.ID,"userA").send_keys("admin")

time.sleep(3)
driver.quit()

# 思考
# 1.什么问题导致的?
# driver的焦点在弹出框页面, 并不在A页面, 无法为你输入admin(找不到用户名输入框)
# 2.如何处理弹出框?
