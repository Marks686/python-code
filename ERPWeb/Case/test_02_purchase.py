# -*- coding:utf-8 -*-

import pytest


def test_purchase_apply(purchase):
    """新增请购单测试用例"""
    purchase.common_login()
    purchase.click_purchase_apply()
    num1 = purchase.get_data_num()  # 在新增之前获取一次数据的数量
    purchase.click_select_goods()
    purchase.click_datermine()
    purchase.click_save_examine()
    num2 = purchase.get_data_num()  # 在新增结束之后获取一次数据的数量
    pytest.assume(num2-num1 == 1)   # 断言新增之后页面上会多一条数据


def test_purchase_order(po):
    """关联请购单新增采购订单"""
    po.common_login()
    po.click_purchase_order()
    num1 = po.get_data_num()  # 在新增之前获取一次数据的数量
    po.click_select_supplier()
    po.click_link_apply()
    po.click_save_examine()
    num2 = po.get_data_num()  # 在新增结束之后获取一次数据的数量
    pytest.assume(num2 - num1 == 1)  # 断言新增之后页面上会多一条数据


if __name__ == '__main__':
    pytest.main()

