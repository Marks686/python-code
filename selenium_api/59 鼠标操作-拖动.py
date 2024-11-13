import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开 drag.html 页面, 把红色方框拖动到蓝色方框上
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/drag.html")
m1 = driver.find_element(By.ID,"div1")
m2 = driver.find_element(By.ID,"div2")
element = ActionChains(driver)
element.drag_and_drop(m1, m2).perform()
time.sleep(3)
driver.quit()
