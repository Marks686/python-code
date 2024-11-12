"""
    1.导包
        导入selenium包 --> from selenium import webdriver
        导入time包 --> import time
    2.创建浏览器驱动 --> driver = webdriver.Chrome()
    3.打开 注册A.html 页面 --> driver.get(url)
    4.通过id定位 --> element = driver.find_element_by_id(id)
    5.使用 send_key() 方法输入内容 --> element.send_keys("admin")
    6.暂停5s --> time.sleep(5)
    7.关闭浏览器 --> driver.quit()
"""

# 1.导包
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# 2.创建浏览器驱动对象
driver = webdriver.Chrome()

# 3.业务操作

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
driver.find_element(By.ID,"userA").send_keys("admin")
driver.find_element(By.ID,"passwordA").send_keys("123456")

# 4.暂停5秒
time.sleep(5)

# 5.关闭驱动对象
driver.quit()
