import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
# driver.find_element(By.XPATH,"//*[text()='访问 新浪 网站']").click()
# driver.find_element(By.XPATH,"//*[contains(@placeholder, '用户名')]").send_keys("admin")
driver.find_element(By.XPATH,"//*[starts-with(@placeholder, '请输入密')]").send_keys("1234")

time.sleep(5)
driver.close()