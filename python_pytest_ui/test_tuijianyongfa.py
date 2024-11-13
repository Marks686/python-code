import pytest


class TestDemo:

# 需求: 使用数据参数化 (推荐用法), 分别打印2组账号和密码: zhangsan / 111111 和 lisi / 222222
#     @pytest.mark.parametrize(("username", "password"), [("zhangsan", "111111"), ("lisi", "222222")])
#     def test_c(self, username, password):
#         print(username + "-----" + password)

    @pytest.mark.parametrize("dict", [{"username": "zhangsan", "password": "111111"}, {"username": "lisi", "password": "222222"}])
    def test_d(self, dict):
        print(dict)
        print(dict["username"])
        print(dict["password"])
#("zhangsan", "111111", "13000000000", "1", "1", "30", "......")
#("lisi", "222222", "13100000000", ??????)
# 推荐的用法是用字典表示参数值
#  {"username": "zhangsan", "password": "111111"}