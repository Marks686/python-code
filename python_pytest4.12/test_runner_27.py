import jsonpath
import pytest
import requests

# 数据
data = [
    {
        "method": "post",
        "url": "http://192.168.10.131:8888/api/private/v1/login",
        "params": None,
        "data": {"username": "admin", "password": "123456"},
        "json": None,
        "files": None,
        "headers": None
    },
    {
        "method": "get",
        "url": "http://192.168.10.131:8888/api/private/v1/users",
        "params": {"pagenum": 1, "pagesize": 1},
        "data": None,
        "json": None,
        "files": None,
        "headers": None
    }
]


class TestRunner:

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        # 请求
        res = requests.request(**case)
        # 打印结果
        print(res.json())
