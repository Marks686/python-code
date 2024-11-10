import jsonpath
import pytest
import requests

# 数据
login_data = [{
    "method": "post",
    "url": "http://192.168.10.131:8888/api/private/v1/login",
    "params": None,
    "data": {"username": "admin", "password": "123456"},
    "json": None,
    "files": None,
    "headers": None
}]
user_list_data = [{
    "method": "get",
    "url": "http://192.168.10.131:8888/api/private/v1/users",
    "params": {"pagenum": 1, "pagesize": 1},
    "data": None,
    "json": None,
    "files": None,
    "headers": None
}]


def get_token():
    res = requests.request(**login_data[0])
    token = jsonpath.jsonpath(res.json(), "$..token")[0]
    return token


class TestRunner:

    @pytest.mark.parametrize("case", login_data)
    def test_login(self, case):
        res = requests.request(**case)
        print(res.json())

    @pytest.mark.parametrize("case", user_list_data)
    def test_user_list(self, case):
        # 调用获取token的函数拿到token值
        token = get_token()
        # 组装 headers, 让请求头中具有token
        case["headers"] = {"Authorization": token}
        res = requests.request(**case)
        print(res.json())