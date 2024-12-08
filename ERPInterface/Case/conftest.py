# -*- coding:utf-8 -*-

import pytest
from Interface.UserInterface.LoginInterface import LoginInterface
from Interface.MemberInterface.MemberInterface import MemberInterface
from Utils.GetKeywords import GetKeywords
from Interface.SalesInterface.SalesInterface import SalesInterface
from Utils.Database import Database


def headers():
    login = LoginInterface()
    result = login.tenant_login("likaixuan","123456Aa")
    token = GetKeywords.get_keyword(result,"token")
    return {"X-Access-Token":token}


@pytest.fixture()
def login():
    return LoginInterface()

@pytest.fixture()
def member():
    return MemberInterface(headers=headers())

@pytest.fixture()
def sales():
    return SalesInterface(headers=headers())

@pytest.fixture()
def db():
    return Database()
