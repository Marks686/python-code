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
time.sleep(2)

alert = driver.switch_to.alert # 切换到alert
print(alert.text)
time.sleep(2)
alert.accept()
# 2
time.sleep(2)
driver.find_element(By.ID,"userA").send_keys("admin")

time.sleep(3)
driver.quit()

