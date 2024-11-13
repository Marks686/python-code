import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

# 需求: 打开A页面, 使用显式等待定位 "延时加载的输入框", 并输入 admin
wait = WebDriverWait(driver, 10, 1) # 10秒内每隔1秒定位一次
element = wait.until(lambda x: x.find_element(By.CSS_SELECTOR,"input[placeholder='延时加载的输入框']"))
element.send_keys("admin")

time.sleep(3)
driver.quit()

# 单个元素定位超时会报错 TimeoutException

