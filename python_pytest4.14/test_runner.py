import logging
import pytest
import requests
from utils.excel_utils import read_excel


class TestRunner:

    # 读测试数据
    data = read_excel()

    @pytest.mark.parametrize("case", data)
    def test_case(self, case):
        # print(case)
        logging.info(case)  # 代替 print() 函数调试运行过程
        # 数据解析: 1.url不存在 2.部分字符串的值需变为字典 3.预期结果这个参数不能再请求中传输, 会报错
        method = case["method"]
        url = "http://192.168.10.131:8888/api/private/v1" + case["path"]
        hearders = eval(case["headers"]) if isinstance(case["headers"], str) else None
        params = eval(case["params"]) if isinstance(case["params"], str) else None
        data = eval(case["data"]) if isinstance(case["data"], str) else None
        json = eval(case["json"]) if isinstance(case["json"], str) else None
        files = eval(case["files"]) if isinstance(case["files"], str) else None

        request_data = {
            "method": method,
            "url": url,
            "headers": hearders,
            "params": params,
            "data": data,
            "json": json,
            "files": files,
        }
        # print(request_data)

        res = requests.request(**request_data)
        # print(res.json())
        assert res.json()["meta"]["msg"] == case["expected"]
