# 导包
import time
from v6.page.login_page import LoginPage
from v6.utils.driver_utils_121 import DriverUtils

# 定义测试类
class TestLogin:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        self.login_page = LoginPage(self.driver)
        self.driver.get("http://192.168.10.139/")

    def teardown(self):
        time.sleep(5)
        DriverUtils.quit_driver()

    # 定义用户不存在的测试方法
    def test_login_account_not_exist(self):
        # 1. 点击首页的"登录"链接, 进入登录页面
        self.login_page.click_login_link()
        # self.driver.find_element_by_class_name("red").click()

        # 2. 输入一个不存在的用户名
        self.login_page.input_username("18800000000")
        # self.driver.find_element_by_id("username").send_keys("18800000000")

        # 3. 输入密码
        self.login_page.input_password("123456")
        # self.driver.find_element_by_id("password").send_keys("123456")

        # 4. 输入验证码
        self.login_page.input_verify_code("8888")
        # self.driver.find_element_by_id("verify_code").send_keys("8888")

        # 5. 点击登录按钮
        self.login_page.click_login_btn()
        # self.driver.find_element_by_name("sbtbutton").click()

        assert "账号不存在!" == self.login_page.get_msg()

        # # 6. 获取错误提示信息
        # msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        # print(msg)
        # # 断言
        # assert "账号不存在!" == msg

    # 定义密码错误的测试方法
    def test_login_password_error(self):
        # 1. 点击首页的"登录"链接, 进入登录页面
        self.login_page.click_login_link()
        # 2. 输入用户名
        self.login_page.input_username("17150312012")
        # 3. 输入一个错误密码
        self.login_page.input_password("error")
        # 4. 输入验证码
        self.login_page.input_verify_code("8888")
        # 5. 点击登录按钮
        self.login_page.click_login_btn()
        # 断言
        assert "密码错误!" == self.login_page.get_msg()
