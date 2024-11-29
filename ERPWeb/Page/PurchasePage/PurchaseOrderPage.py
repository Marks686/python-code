# -*- coding:utf-8 -*-

# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By as by
from Page.UserPage.ErpLoginPage import ErpLoginPage
import re
import time


class ProcureOrderPage(ErpLoginPage):
    """表现层"""
    # 采购管理点击下拉
    procure_button = (by.XPATH, '//div[@class="ant-layout-sider-children"]/ul/li[3]')

    # 获取页面条数
    data_num = (by.CSS_SELECTOR, '.ant-pagination-total-text')

    # 采购订单按钮
    purchase_order = (by.CSS_SELECTOR, 'a[target="采购订单"]')

    # 请购单新增按钮
    new_add = (by.XPATH, '//div[@class="table-operator"]/button[1]')

    # 点击引导关闭
    skip_button = (by.CLASS_NAME, 'introjs-skipbutton')

    # 点击选择供应商按钮
    select_supplier = (by.CSS_SELECTOR, '#organId .ant-select-selection__rendered')

    # 选择小米供应商
    select_xiaomi = (by.CSS_SELECTOR, '.ant-select-dropdown-menu-item')

    # 点击关联请购单
    link_apply = (by.CSS_SELECTOR, '.ant-input-search-icon > svg')

    # 选择第一个请购单
    first_apply = (by.CSS_SELECTOR, '.ant-table-row:nth-child(1) .ant-radio-input')

    # 确定按钮
    determine = (by.CSS_SELECTOR, '.ant-btn-primary:nth-child(2)')

    # 选择单据明细
    detailed = (by.CSS_SELECTOR, '.ant-table-tbody:nth-child(3) .ant-checkbox-input')

    # 保存并审核
    save_examine = (by.CSS_SELECTOR, '.ant-modal-footer > .ant-btn:nth-child(2)')


    """操作层"""
    def click_purchase_order(self):
        """点击进入到采购订单"""
        self.click(self.procure_button)
        time.sleep(2)
        self.click(self.purchase_order)

    def click_select_supplier(self):
        """点击选择供应商"""
        self.click(self.new_add)
        self.click(self.skip_button)
        self.click(self.select_supplier)
        self.click(self.select_xiaomi)

    def click_link_apply(self):
        """点击请购单，选择对应的订购单并确认"""
        self.click(self.link_apply)
        self.click(self.first_apply)
        self.click(self.determine)
        self.click(self.detailed)
        self.click(self.determine)

    def click_save_examine(self):
        """保存并审核"""
        self.click(self.save_examine)
        # self.refresh()

    def get_data_num(self):
        """获取页面的数据"""
        text = self.get_element_text(self.data_num)
        text = text[4:]
        num = int(re.findall(r'\d+',text)[0])
        return num


if __name__ == '__main__':
    po = ProcureOrderPage()

    po.common_login()
    po.click_purchase_order()
    po.click_select_supplier()
    po.click_link_apply()
    po.click_save_examine()