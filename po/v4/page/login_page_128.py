class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # 点击首页的"登录"链接, 进入登录页面
    def click_login_link(self):
        return self.driver.find_element_by_class_name("red").click()

    # 输入用户名
    def input_username(self, username):
        return self.driver.find_element_by_id("username").send_keys(username)

    # 输入密码
    def input_password(self, password):
        return self.driver.find_element_by_id("password").send_keys(password)

    # 输入验证码
    def input_verify_code(self, code):
        return self.driver.find_element_by_id("verify_code").send_keys(code)

    # 点击登录按钮
    def click_login_btn(self):
        return self.driver.find_element_by_name("sbtbutton").click()

    # 获取提示信息
    def get_msg(self):
        msg = self.driver.find_element_by_css_selector(".layui-layer-content").text
        return msg