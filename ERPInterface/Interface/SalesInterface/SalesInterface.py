# -*- coding:utf-8 -*-

from Utils.SendMethod import SendMethod
from Utils.TimeFormat import *
from Utils.GetKeywords import GetKeywords


class SalesInterface(object):

    def __init__(self, headers):
        self.url = "http://192.168.10.150"
        self.headers = headers

    def build_number(self):
        """生成单号的方法"""
        url = self.url + "/jshERP-boot/sequence/buildNumber"
        method = "get"
        result = SendMethod.send_method(url=url, method=method, headers=self.headers)
        num = GetKeywords.get_keyword(result, 'defaultNumber')
        return num

    def add_sales_order(self):
        """新增销售订单的接口"""
        url = self.url + "/jshERP-boot/depotHead/addDepotHeadAndDetail"
        method = "post"
        payload = {"info": "{\"defaultNumber\":\"XSDD00000000768\","
                           "\"organId\":169,\"operTime\":\"2024-08-13 16:24:24\","
                           "\"number\":\"XSDD00000000768\",\"discount\":0,"
                           "\"discountMoney\":0,\"discountLastMoney\":0,"
                           "\"accountId\":19,\"changeAmount\":0,\"type\":\"其它\","
                           "\"subType\":\"销售订单\",\"totalPrice\":0,"
                           "\"accountIdList\":\"\",\"accountMoneyList\":\"\","
                           "\"fileName\":\"\",\"salesMan\":\"\",\"status\":\"1\"}",
                   "rows": "[{\"id\":\"17235374640920265462\",\"hiddenKey\":\"\","
                           "\"name\":\"小米剃须刀\",\"standard\":null,\"model\":null,"
                           "\"color\":null,\"materialOther\":\"\",\"stock\":993,"
                           "\"unit\":\"个\",\"sku\":\"\",\"operNumber\":1,"
                           "\"unitPrice\":null,\"allPrice\":null,\"taxRate\":0,"
                           "\"taxMoney\":0,\"taxLastMoney\":null,\"remark\":\"\","
                           "\"barCode\":\"1002\",\"depotId\":\"\"}]"}

        info = eval(payload['info'])  # 取出info修改为dict
        num = self.build_number()
        # 构造新的info
        info['defaultNumber'] = "XSDD" + str(num)
        info["number"] = "XSDD" + str(num)
        info["operTime"] = get_now_time()

        # 把构造之后的info放回payload
        payload["info"] = str(info)

        return SendMethod.send_method(url=url, method=method, json=payload, headers=self.headers)

    def find_link_number(self):
        """查找关联的销售订单"""
        url = self.url + "/jshERP-boot/depotHead/list?" + "search=%7B%22number%22:%22%22,%22materialParam%22:%22%22,%22type%22:%22%E5%85%B6%E5%AE%83%22,%22subType%22:%22%E9%94%80%E5%94%AE%E8%AE%A2%E5%8D%95%22,%22status%22:%221,3%22%7D&column=createTime&order=desc&field=id,,organName,number,materialsList,operTimeStr,userName,materialCount,totalPrice,totalTaxLastMoney,status&currentPage=1&pageSize=10"
        method = "get"
        result = SendMethod.send_method(url=url,method=method,headers=self.headers)
        return GetKeywords.get_keyword(result,"defaultNumber")


    def add_sales_out(self):
        """新增销售出库"""
        url = self.url + "/jshERP-boot/depotHead/addDepotHeadAndDetail"
        method = "post"
        payload = {"info":"{\"defaultNumber\":\"XSCK00000000776\","
                          "\"organId\":169,\"operTime\":\"2024-08-13 16:44:19\","
                          "\"number\":\"XSCK00000000776\","
                          "\"linkNumber\":\"XSDD00000000774\",\"discount\":0,"
                          "\"discountMoney\":0,\"discountLastMoney\":0,"
                          "\"otherMoney\":0,\"accountId\":19,"
                          "\"changeAmount\":0,\"debt\":0,\"type\":\"出库\","
                          "\"subType\":\"销售\",\"totalPrice\":0,"
                          "\"accountIdList\":\"\",\"accountMoneyList\":\"\","
                          "\"fileName\":\"\",\"salesMan\":\"\",\"status\":\"1\"}",
                   "rows":"[{\"id\":\"392\",\"barCode\":\"1002\",\"name\":\"小米剃须刀\","
                          "\"standard\":\"\",\"model\":\"\",\"color\":\"\",\"materialOther\":\"\","
                          "\"stock\":\"993\",\"unit\":\"个\",\"snList\":\"\",\"batchNumber\":\"\","
                          "\"expirationDate\":\"\",\"sku\":\"\",\"preNumber\":\"1\",\"finishNumber\":\"0\","
                          "\"operNumber\":\"1\",\"unitPrice\":\"\",\"allPrice\":\"\",\"taxRate\":\"0\","
                          "\"taxMoney\":\"0\",\"taxLastMoney\":\"\",\"remark\":\"\",\"linkId\":\"392\","
                          "\"depotId\":\"18\"}]"}

        info = eval(payload['info'])  # 取出info修改为dict
        num = self.build_number()
        # 构造新的info
        info['defaultNumber'] = "XSCK" + str(num)
        info["number"] = "XSCK" + str(num)
        info["operTime"] = get_now_time()
        info["linkNumber"] = self.find_link_number()

        # 把构造之后的info放回payload
        payload["info"] = str(info)

        return SendMethod.send_method(url=url,method=method,json=payload,headers=self.headers)


if __name__ == '__main__':
    from Interface.UserInterface.LoginInterface import LoginInterface
    from Utils.GetKeywords import GetKeywords

    res = LoginInterface().tenant_login("chen-888", "123456Aa")
    headers = {"X-Access-Token": "d240054b50ba41e6a8a948c7e29dcae5_132"}

    sales = SalesInterface(headers)
    print(sales.add_sales_order())
    print(sales.add_sales_out())