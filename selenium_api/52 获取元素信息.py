import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")


# 需求: 打开A页面, 完成以下操作:
# 1.获取用户名输入框的大小
print(driver.find_element(By.ID,"userA").size)
# 2.获取页面上第一个超链接的文本内容
print(driver.find_element(By.TAG_NAME,"a").text)
# 3.获取页面上第一个超链接的地址
print(driver.find_element(By.TAG_NAME,"a").get_attribute("href"))
# 4.判断页面中的span标签是否可见
print(driver.find_element(By.TAG_NAME,"span").is_displayed())
# 5.判断页面中的取消按钮是否可用
print(driver.find_element(By.XPATH,"/html/body/div/fieldset/form/p[5]/button").is_enabled())
# 6.判断页面中的'旅游'对应的复选框是否为选中状态
print(driver.find_element(By.ID,"lyA").is_selected())

time.sleep(3)
driver.quit()
