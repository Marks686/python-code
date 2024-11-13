import time
from selenium import webdriver

driver = webdriver.Chrome()

# 需求: 打开A页面
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")

# js1 滚动到最底部
js1 = "window.scrollTo(0, 10000)"
# js2 滚动到最顶部
js2 = "window.scrollTo(0, 0)"
# 执行第一个脚本
time.sleep(2)
driver.execute_script(js1)
# 执行第二个脚本
time.sleep(2)
driver.execute_script(js2)

time.sleep(3)
driver.quit()

