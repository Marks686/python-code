# -*- coding:utf-8 -*-

import pytest

def test_login(login):
    login.open_login_url()
    login.send_user_name("chen-888")
    login.send_password("123456Aa")
    login.send_code()
    login.click_button()
    username = login.get_index_user_name_text()
    # 断言,登录成功之后用户名和登录的用户名是一致的
    pytest.assume("chen-888" in username)

if __name__ == '__main__':
    pytest.main()