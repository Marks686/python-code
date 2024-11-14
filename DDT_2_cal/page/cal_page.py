from selenium.webdriver.common.by import By
from base.base_action import BaseAction


class CalPage(BaseAction):

    # 数字 按钮
    digit_btn = By.ID, "simple{}"
    # 加号 按钮
    add_btn = By.ID, "simpleAdd"
    # 等号 按钮
    eq_btn = By.ID, "simpleEqual"
    # 计算结果
    result = By.ID, "resultIpt"

    # 点击数字
    def click_digit_btn(self, num):
        return self.find_el_num(self.digit_btn, num).click()
    # 点击加号
    def click_add_btn(self):
        return self.click(self.add_btn)
    # 点击等号
    def click_eq_btn(self):
        return self.click(self.eq_btn)
    # 获取计算结果
    def get_result(self):
        return self.find_el(self.result).get_attribute("value")



