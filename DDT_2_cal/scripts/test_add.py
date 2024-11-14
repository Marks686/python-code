# 导包
import time
import pytest
from base.base_analyze import analyze_data
from page.cal_page import CalPage
from utils.driver_utils import DriverUtils

# 定义测试类
class TestCal:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        self.cal_page = CalPage(self.driver)
        self.driver.get("http://cal.apple886.com/")

    def teardown(self):
        time.sleep(5)
        DriverUtils.quit_driver()

    # [{"num1": 1, "num2": 1, "result": 2}, {"num1": 1, "num2": 2, "result": 3}]
    # [{"data": [1, 1],"result": 2}, {"data": [1, 2],"result": 3}, {"data": [1, 2, 3],"result": 6}]
    @pytest.mark.parametrize("params", analyze_data("cal_data.json"))
    def test_add(self, params):
        # self.cal_page.click_digit_btn(params["data"][0])
        # self.cal_page.click_add_btn()
        # self.cal_page.click_digit_btn(params["data"][1])
        for i in params["data"]:
            self.cal_page.click_digit_btn(i)
            self.cal_page.click_add_btn()
        self.cal_page.click_eq_btn()
        assert str(params["result"]) == self.cal_page.get_result()



