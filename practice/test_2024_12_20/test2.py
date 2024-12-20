import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

element = driver.find_element(By.ID, "userA")
element.send_keys("admin")
element = driver.find_element(By.ID, "passwordA")
element.send_keys("123456")
time.sleep(3)
driver.quit()