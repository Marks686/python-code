 # -*- coding:utf-8 -*-
from Utils.SendMethod import SendMethod
from Utils.Encryption import *


class LoginInterface(object):

    def __init__(self):
        self.url = "http://192.168.10.150"

    def tenant_login(self,username,password):
        """租户登录"""
        url = self.url + "/jshERP-boot/user/login"
        method = "post"
        payload = {"loginName":username,
                   "password":md5_hash(password)}

        return SendMethod.send_method(url=url,method=method,json=payload)




if __name__ == '__main__':
    login = LoginInterface()
    print(login.tenant_login(
        "likaixuan","123456Aa"
    ))