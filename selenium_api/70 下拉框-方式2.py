import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

# 需求: 打开A页面,完成以下下拉框操作
# 1. 暂停2s, 选择广州
# 2. 暂停2s, 选择上海
# 3. 暂停2s, 选择北京
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

select = Select(driver.find_element(By.ID,"selectA"))
# 1
time.sleep(2)
select.select_by_index(2)
# 2
time.sleep(2)
select.select_by_value("sh")
# 3
time.sleep(2)
select.select_by_visible_text("北京")

time.sleep(3)
driver.quit()


