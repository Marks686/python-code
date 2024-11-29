# -*- coding:utf-8 -*-

import pytest
from Page.UserPage.ErpLoginPage import ErpLoginPage
from Page.PurchasePage.PurchaseApplyPage import PurchaseApplyPage
from Page.PurchasePage.PurchaseOrderPage import ProcureOrderPage


@pytest.fixture()
def login():
    return ErpLoginPage()

@pytest.fixture()
def purchase():
    return PurchaseApplyPage()



@pytest.fixture(name="po")
def purchase_order():
    return ProcureOrderPage()

