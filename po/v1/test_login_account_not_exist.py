# 账号不存在
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化浏览器驱动
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://192.168.10.139/")

# 1. 点击首页的"登录"链接, 进入登录页面
driver.find_element(By.CLASS_NAME,"red").click()
# 2. 输入一个不存在的用户名
driver.find_element(By.ID,"username").send_keys("18800000000")
# 3. 输入密码
driver.find_element(By.ID,"password").send_keys("123456")
# 4. 输入验证码
driver.find_element(By.ID,"verify_code").send_keys("8888")
# 5. 点击登录按钮
driver.find_element(By.NAME,"sbtbutton").click()
# 6. 获取错误提示信息
msg = driver.find_element(By.CSS_SELECTOR,".layui-layer-content").text
print(msg)

# 关闭浏览器驱动
time.sleep(5)
driver.quit()