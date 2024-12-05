# -*- coding:utf-8 -*-

"""
1.这是登录页面的Page类
2.这个类会封装登录所需要的表现层和操作层
"""
from Common.Base import Base
from selenium.webdriver.common.by import By as by
from Common.GetCodeImg import GetImgText

class ErpLoginPage(Base):
    """表现层"""
    # 元素、链接...
    url = "http://192.168.10.150/user/login"
    login_name = (by.ID,"loginName")
    password = (by.ID,"password")
    input_code = (by.ID,"inputCode")

    # 点击按钮
    # span[class="ant-form-item-children"]>button
    # //span[@class="ant-form-item-children"]/button
    login_button = (by.CSS_SELECTOR,'span[class="ant-form-item-children"]>button')

    # 验证码
    img_code = (by.XPATH,'//div[@class="ant-col ant-col-10"]/img')

    # 登录之后的引导弹窗
    close_button = (by.CLASS_NAME,'introjs-skipbutton')

    # 登录之后的用户名
    index_user_name = (by.XPATH,'//span[@class="action ant-dropdown-link user-dropdown-menu ant-dropdown-trigger"]/span')


    """操作层"""
    def open_login_url(self):
        self.open_url(self.url)

    def get_code_link(self):
        """获取验证码的base64编码"""
        code_link = self.get_attribute(self.img_code,"src")
        return code_link

    def get_code_text(self):
        """获取验证码的文本"""
        text = GetImgText(self.get_code_link()).get_dddd_text()
        return text

    def send_user_name(self,username):
        """输入用户名"""
        self.send_keys(self.login_name,username)

    def send_password(self,password):
        """输入密码"""
        self.send_keys(self.password,password)

    def send_code(self):
        """输入验证码"""
        code = self.get_code_text()
        print(code)
        self.send_keys(self.input_code,code)

    def click_button(self):
        """点击登录按钮"""
        self.click(self.login_button)
        self.click(self.close_button)  # 登录成功之后关闭引导的弹窗

    def get_index_user_name_text(self):
        """获取登录之后的用户名"""
        return self.get_element_text(self.index_user_name)


    def common_login(self):
        """公共的登录的逻辑，所有需要登录的都可以从这里获取"""
        self.open_login_url()
        self.send_user_name("likaixuan")
        self.send_password("123456Aa")
        self.send_code()
        self.click_button()


if __name__ == '__main__':
    erp = ErpLoginPage()
    erp.open_login_url()
    erp.send_user_name("likaixuan")
    erp.send_password("123456Aa")
    erp.send_code()
    erp.click_button()
