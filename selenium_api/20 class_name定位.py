
# 1.导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2.创建浏览器驱动对象
driver = webdriver.Chrome()

# 3.业务操作
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
driver.find_element(By.CLASS_NAME,"telA").send_keys("1231312312312312")
driver.find_element(By.CLASS_NAME,"dzyxA").send_keys("12313@qq.com")

# 4.暂停5秒
time.sleep(5)

# 5.关闭驱动对象
driver.quit()
