import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 隐式等待10秒, 以防新浪窗口加载慢, 定位不到输入框
driver.implicitly_wait(10)

# 1. 打开A页面, 获取当前窗口句柄(拿到的是A页面的句柄)
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

print("当前A页面窗口句柄:", driver.current_window_handle)
# 2. 在A页面点击"访问 新浪 网站" 这个超链接, 获取所有窗口句柄
driver.find_element(By.ID,"fw").click()
handles = driver.window_handles
print("所有窗口句柄:", handles)
# 3. 根据句柄, 切换到新浪窗口, 对输入框输入 "新浪搜索"
driver.switch_to.window(handles[1])
time.sleep(1)
driver.find_element(By.CLASS_NAME,"inp-txt").clear()
time.sleep(1)
driver.find_element(By.CLASS_NAME,"inp-txt").send_keys("新浪搜索")
time.sleep(2)
# 4. 切换回原本窗口(A页面), 输入用户名 admin
driver.switch_to.window(handles[0])
driver.find_element(By.ID,"userA").send_keys("admin")

time.sleep(3)
driver.quit()
