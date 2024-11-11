# 需求: 通过程序, 启动浏览器, 并打开百度首页, 暂停3秒, 关闭浏览器
import time

from selenium import webdriver

# 1.导包

# 2.创建浏览器驱动对象
drive = webdriver.Chrome()


# 3.打开百度首页
drive.get("https://www.baidu.com")

# 4.暂停3秒
time.sleep(2)


# 5.关闭驱动对象
drive.quit()