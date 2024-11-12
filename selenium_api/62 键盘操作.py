import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("file:///C:/Users/57769/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
# 1. 输入用户名 admin1, 暂停2s, 删除1
element = driver.find_element_by_id("userA")
element.send_keys("admin1")
time.sleep(2)
element.send_keys(Keys.BACK_SPACE)
# 2. 全选用户名 admin 暂停2s
element.send_keys(Keys.CONTROL, "a")
time.sleep(2)
# 3. 复制用户名 admin 暂停2s
element.send_keys(Keys.CONTROL, "c")
time.sleep(2)
# 4. 粘贴到电话输入框
driver.find_element_by_id("telA").send_keys(Keys.CONTROL, "v")

time.sleep(5)
driver.quit()
