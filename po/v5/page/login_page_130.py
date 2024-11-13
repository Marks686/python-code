from selenium.webdriver.common.by import By


class LoginPage:

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

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, feature):
        return self.driver.find_element(*feature)
        # return self.driver.find_elment(feature[0], feature[1])

    # 点击首页的"登录"链接, 进入登录页面
    def click_login_link(self):
        return self.find_el(self.login_link_btn).click()
        # return self.driver.find_elment(self.login_link_btn[0], self.login_link_btn[1]).click()
        # return self.driver.find_element_by_class_name("red").click()

    # 输入用户名
    def input_username(self, username):
        return self.find_el(self.username_input).send_keys(username)
        # return self.driver.find_element_by_id("username").send_keys(username)

    # 输入密码
    def input_password(self, password):
        return self.find_el(self.password_input).send_keys(password)
        # return self.driver.find_element_by_id("password").send_keys(password)

    # 输入验证码
    def input_verify_code(self, code):
        return self.find_el(self.verify_code_input).send_keys(code)
        # return self.driver.find_element_by_id("verify_code").send_keys(code)

    # 点击登录按钮
    def click_login_btn(self):
        return self.find_el(self.login_btn).click()
        # return self.driver.find_element_by_name("sbtbutton").click()

    # 获取提示信息
    def get_msg(self):
        return self.find_el(self.msg_info).text
        # msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        # return msg