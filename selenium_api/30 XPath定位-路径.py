import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")
#driver.get("file:///C:/Users/57769/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 定位用户名输入框, 输入 admin
driver.find_element(By.XPATH,"/html/body/div/fieldset/form/p[1]/input").send_keys("admin")
# 暂停3s
time.sleep(3)
# 定位密码输入框, 输入 123
driver.find_element(By.XPATH,"//*[@id='passwordA']").send_keys("123")

time.sleep(5)
driver.close()

