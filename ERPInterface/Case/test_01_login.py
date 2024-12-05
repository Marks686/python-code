# -*- coding:utf-8 -*-

import pytest
from Utils.GetKeywords import GetKeywords

def test_01_login(login):
    result = login.tenant_login("chen-888","123456Aa")
    print(result)
    username = GetKeywords.get_keyword(result,"username")
    status_code = GetKeywords.get_keyword(result,"status_code")
    pytest.assume(status_code==200)
    pytest.assume(username == "chen-888")

if __name__ == '__main__':
    pytest.main()
