import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

# 需求: 使用cookie 实现跳过百度登录
# 1.手动登录百度, 获取cookie
# 2.请求百度, 并且带上cookie

# 没有cookie的时候
driver.get("http://www.baidu.com")
# 添加cookie操作  value值要根据你登录百度后 BDUSS所对应的 value去调整
driver.add_cookie({"name": "BDUSS",
                   "value": "VZMUEl0WFJQYkxNSXk0c0VMUk5ZNGYteWVYNG01aVJtZXFCV056alk5M3V3SUZlSVFBQUFBJCQAAAAAAAAAAAEAAAC2KUFmTFhKX0pheQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO4zWl7uM1peQ"
                   })
time.sleep(3)
# 刷新, 再次请求百度首页, 验证是否带上身份信息
driver.refresh()

time.sleep(3)
driver.quit()
