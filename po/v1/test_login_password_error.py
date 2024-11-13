# 密码错误
import time
from selenium import webdriver

# 实例化浏览器驱动
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://localhost/")

# 1. 点击首页的"登录"链接, 进入登录页面
driver.find_element_by_class_name("red").click()
# 2. 输入用户名
driver.find_element_by_id("username").send_keys("17150312012")
# 3. 输入一个错误密码
driver.find_element_by_id("password").send_keys("error")
# 4. 输入验证码
driver.find_element_by_id("verify_code").send_keys("8888")
# 5. 点击登录按钮
driver.find_element_by_name("sbtbutton").click()
# 6. 获取错误提示信息
msg = driver.find_element_by_css_selector(".layui-layer-content").text
print(msg)

# 关闭浏览器驱动
time.sleep(5)
driver.quit()