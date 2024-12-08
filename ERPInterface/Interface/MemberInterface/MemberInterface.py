# -*- coding:utf-8 -*-
from Utils.SendMethod import SendMethod

class MemberInterface(object):

    def __init__(self,headers):
        self.url = "http://192.168.10.150"
        self.headers = headers

    def add_member(self,supplier,telephone=None):
        url = self.url + "/jshERP-boot/supplier/add"
        method = "post"
        payload = {"supplier":supplier,
                   "contacts":"李四","telephone":telephone,
                   "phoneNum":"15627261551","email":"1131982165@qq.com",
                   "sort":"3","description":"1234","type":"会员"}

        return SendMethod.send_method(url=url,method=method,json=payload,headers=self.headers)


    def del_member(self,del_id):
        url = self.url + f"/jshERP-boot/supplier/delete?id={del_id}"
        method = "delete"
        return SendMethod.send_method(url=url,method=method,headers=self.headers)

    def find_member(self):
        url = self.url + "/jshERP-boot/supplier/list?search=%7B%22supplier%22:%22%22,%22type%22:%22%E4%BC%9A%E5%91%98%22,%22telephone%22:%22%22,%22phonenum%22:%22%22%7D&column=createTime&order=desc&field=id,,,action,supplier,contacts,telephone,phoneNum,email,advanceIn,sort,enabled&currentPage=1&pageSize=10"
        method = "get"
        return SendMethod.send_method(url=url,method=method,headers=self.headers)


if __name__ == '__main__':
    from Interface.UserInterface.LoginInterface import LoginInterface
    from Utils.GetKeywords import GetKeywords
    res = LoginInterface().tenant_login("likaixuan","123456Aa")
    print(res)
    token = GetKeywords.get_keyword(res,"token")

    headers = {"X-Access-Token":token}
    member = MemberInterface(headers)
    # print(member.add_member(1234))
    print(member.find_member())