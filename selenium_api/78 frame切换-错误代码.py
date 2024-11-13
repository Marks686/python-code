import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开"注册实例"页面
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html")
# 1.填写主页面的用户名 admin
time.sleep(2)
driver.find_element(By.ID,"userA").send_keys("admin")
# 2.填写注册页面A中的用户名 adminA
time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='userA']").send_keys("adminA")    # 这一步定位出错了!!!
# 3.填写注册页面B中的用户名 adminB

time.sleep(3)
driver.quit()

# 当前页面内无法定位注册页面A和B中的元素

