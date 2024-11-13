# 导包
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定义测试类
class TestLogin:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://192.168.10.139/")

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 定义用户不存在的测试方法
    def test_login_account_not_exist(self):
        # 1. 点击首页的"登录"链接, 进入登录页面
        self.driver.find_element(By.CLASS_NAME,"red").click()
        # 2. 输入一个不存在的用户名
        self.driver.find_element(By.ID,"username").send_keys("18800000000")
        # 3. 输入密码
        self.driver.find_element(By.ID,"password").send_keys("123456")
        # 4. 输入验证码
        self.driver.find_element(By.ID,"verify_code").send_keys("8888")
        # 5. 点击登录按钮
        self.driver.find_element(By.NAME,"sbtbutton").click()
        # 6. 获取错误提示信息
        msg = self.driver.find_element(By.CSS_SELECTOR,".layui-layer-content").text
        print(msg)
        # 断言
        assert "账号不存在!" == msg

    # 定义密码错误的测试方法
    def test_login_password_error(self):
        # 1. 点击首页的"登录"链接, 进入登录页面
        self.driver.find_element(By.CLASS_NAME,"red").click()
        # 2. 输入用户名
        self.driver.find_element(By.ID,"username").send_keys("17150312012")
        # 3. 输入一个错误密码
        self.driver.find_element(By.ID,"password").send_keys("error")
        # 4. 输入验证码
        self.driver.find_element(By.ID,"verify_code").send_keys("8888")
        # 5. 点击登录按钮
        self.driver.find_element(By.ID,"sbtbutton").click()
        # 6. 获取错误提示信息
        msg = self.driver.find_element(By.CSS_SELECTOR,".layui-layer-content").text
        print(msg)
        # 断言
        assert "密码错误!" == msg
