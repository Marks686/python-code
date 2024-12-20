import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 暂停三秒
time.sleep(3)
# 关闭驱动
driver.quit()