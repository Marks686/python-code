import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# 需求: 打开 A 页面, 完成以下操作
# 1.输入用户名 admin
# 2.截图保存
driver.get("file:///D:/%E7%99%BE%E5%BA%A6%E7%BD%91%E7%9B%98/9-UI%E8%87%AA%E5%8A%A8%E5%8C%96/pagetest/pagetest/%E6%B3%A8%E5%86%8CA.html")


# 1
driver.find_element(By.ID,"userA").send_keys("admin")
# 2
time.sleep(1)
# 每次都是用固定文件名, 会股改上一次生成的图片文件
# driver.get_screenshot_as_file("./png/123.png")  # 需要提前创建 png 目录

# 使用时间去格式化文件名, 可以使每次截图保存的文件名都不同, 不会覆盖之前保存的文件, 更有效
imgpath = "./png/test_{}.png".format(time.strftime("%Y%m%d%H%M%S"))
driver.get_screenshot_as_file(imgpath)

time.sleep(3)
driver.quit()
