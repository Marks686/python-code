import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

# 利用元素属性通过XPath 定位用户名输入框, 并输入 admin
# driver.find_element_by_xpath("//*[@name='userA']").send_keys("admin")
# driver.find_element_by_xpath("//*[@id='userA']").send_keys("admin")
# driver.find_element_by_xpath("//*[@placeholder='请输入用户名']").send_keys("admin")
driver.find_element(By.XPATH,"//*[@type='text']").send_keys("admin")

time.sleep(5)
driver.close()