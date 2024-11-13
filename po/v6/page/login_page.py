from selenium.webdriver.common.by import By
from v6.base.base_action_132 import BaseAction


class LoginPage(BaseAction):

    # 登录链接 按钮
    login_link_btn = By.CLASS_NAME, "red"
    # 用户名 输入框
    username_input = By.ID, "username"
    # 密码 输入框
    password_input = By.ID, "password"
    # 验证码 输入框
    verify_code_input = By.ID, "verify_code"
    # 登录 按钮
    login_btn = By.NAME, "sbtbutton"
    # 提示信息
    msg_info = By.CSS_SELECTOR, ".layui-layer-content"

    # 点击首页的"登录"链接, 进入登录页面
    def click_login_link(self):
        return self.click(self.login_link_btn)
        # return self.find_el(self.login_link_btn).click()

    # 输入用户名
    def input_username(self, content):
        return self.input(self.username_input, content)
        # return self.find_el(self.username_input).send_keys(username)

    # 输入密码
    def input_password(self, content):
        return self.input(self.password_input, content)
        # return self.find_el(self.password_input).send_keys(password)

    # 输入验证码
    def input_verify_code(self, content):
        return self.input(self.verify_code_input, content)
        # return self.find_el(self.verify_code_input).send_keys(code)

    # 点击登录按钮
    def click_login_btn(self):
        return self.click(self.login_btn)
        # return self.find_el(self.login_btn).click()

    # 获取提示信息
    def get_msg(self):
        return self.find_el(self.msg_info).text
