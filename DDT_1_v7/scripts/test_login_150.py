# 导包
import time
import pytest
from base.base_analyze_149 import analyze_data
from page.login_page_132 import LoginPage
from utils.driver_utils_121 import DriverUtils

# 定义测试类
class TestLogin:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        self.login_page = LoginPage(self.driver)
        self.driver.get("http://192.168.10.139/")

    def teardown(self):
        time.sleep(5)
        DriverUtils.quit_driver()

    # 定义测试登录的方法, 实现脚本参数化, 从 json文件中读取数据
    @pytest.mark.parametrize("params", analyze_data("login_data.json"))
    def test_login(self, params):
        self.login_page.click_login_link()
        self.login_page.input_username(params["username"])
        self.login_page.input_password(params["password"])
        self.login_page.input_verify_code(params["code"])
        self.login_page.click_login_btn()
        assert params["msg"] == self.login_page.get_msg()

