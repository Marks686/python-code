import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 打开注册A页面，完成以下操作
# 1.通过脚本执行输入用户名：admin；密码：123456；电话号码：18611111111；电子邮件：123@qq.com
# 2.间隔3秒，修改电话号码为：18600000000
# 3.间隔3秒，点击‘注册’按钮
# 4.间隔3秒，关闭浏览器
# ps: 元素定位方法不限
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 1
driver.find_element(By.ID,"userA").send_keys("admin")
driver.find_element(By.ID,"passwordA").send_keys("123456")
driver.find_element(By.ID,"telA").send_keys("18611111111")
driver.find_element(By.NAME,"emailA").send_keys("123@qq.com")
# 2
time.sleep(3)
driver.find_element(By.ID,"telA").clear()
driver.find_element(By.ID,"telA").send_keys("18600000000")
# 3
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"body > div > fieldset > form > p:nth-child(5) > button").click()
# 4
time.sleep(3)
driver.close()
