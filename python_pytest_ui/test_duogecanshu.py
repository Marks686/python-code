import pytest


class TestDemo:

# 需求: 使用数据参数化 (多个参数), 分别打印2组账号和密码: zhangsan / 111111 和 lisi / 222222
    @pytest.mark.parametrize(("username", "password"), [("zhangsan", "111111"), ("lisi", "222222")])
    def test_c(self, username, password):
        print(username + "-----" + password)

# 使用元组可以传多个值  ("zhangsan", "111111"),   列表行不行?