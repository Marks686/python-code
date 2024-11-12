import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

# # maximize_window() 浏览器窗口最大化
# driver.maximize_window()

## set_window_size() 设置窗口大小(单位:像素点)   set_window_position()  设置窗口的位置
# driver.set_window_size(300, 300)
# driver.set_window_position(300, 300)

## back() 后退 forward() 前进 refresh() 刷新
# driver.back()
# driver.forward()
# time.sleep(3)
# driver.refresh()

## title 获取页面标题     current_url  获取当前页面url
print("页面标题:", driver.title)
print("当前页面地址:", driver.current_url)

## driver.close()   关闭当前浏览器窗口  ==> 执行结果, 留下了新浪网站, 关闭了注册A页面
# time.sleep(3)
# driver.find_element_by_link_text("访问 新浪 网站").click()
# time.sleep(3)
# driver.close()

### 序号 30~48 的脚本应该使用 driver.quit() 关闭浏览器驱动 而不是 driver.close()
## driver.quit()    关闭浏览器驱动对象(关闭浏览器)    ==> 执行结果, 关闭所有窗口, 关闭浏览器驱动
time.sleep(3)
driver.find_element(By.LINK_TEXT,"访问 新浪 网站").click()
time.sleep(3)
driver.quit()
