# -*- coding:utf-8 -*-

from Page.UserPage.ErpLoginPage import ErpLoginPage
from selenium.webdriver.common.by import By as by
import time
import re

class PurchaseApplyPage(ErpLoginPage):
    """表现层"""
    # 采购管理
    purchase_button = (by.XPATH,'//div[@class="ant-layout-sider-children"]/ul/li[3]')

    # 请购单
    purchase_apply = (by.CSS_SELECTOR,'a[target="请购单"]')

    # 定位新增的按钮
    new_add = (by.CSS_SELECTOR,'.table-operator>button:nth-child(1)')

    # 引导关闭
    skip_button = (by.CLASS_NAME,'introjs-skipbutton')

    # 点击选择商品
    find_goods = (by.CSS_SELECTOR,'button[class="ant-btn ant-btn-icon-only"]')

    # 选中商品
    select_goods = (by.CSS_SELECTOR,'.ant-table-tbody:nth-child(3) .ant-checkbox-input')

    # 确定的按钮
    datermine = (by.CSS_SELECTOR,'.ant-btn-primary:nth-child(2)')

    # 保存并审核
    save_examine = (by.CSS_SELECTOR,'.ant-modal-footer>button:nth-child(2)')

    # 数据量
    data_num = (by.CLASS_NAME,"ant-pagination-total-text")




    """操作层"""
    def click_purchase_apply(self):
        """点击进入到请购单"""
        self.click(self.purchase_button)
        time.sleep(2)
        self.click(self.purchase_apply)

    def click_select_goods(self):
        """点击新增并选择商品"""
        self.click(self.new_add)
        self.click(self.skip_button)
        self.click(self.find_goods)
        self.click(self.select_goods)

    def click_datermine(self):
        """点击确定"""
        self.click(self.datermine)

    def click_save_examine(self):
        """点击保存并审核"""
        self.click(self.save_examine)
        # self.refresh()

    def get_data_num(self):
        """获取页面的数据"""
        text = self.get_element_text(self.data_num)
        text = text[4:]
        num = int(re.findall(r'\d+',text)[0])
        return num


if __name__ == '__main__':
    pa = PurchaseApplyPage()
    pa.common_login()
    pa.click_purchase_apply()
    pa.click_select_goods()
    pa.click_datermine()
    pa.click_save_examine()
    pa.get_data_num()

