import pytest
from demo import demo


class TestDemo:

    # def test_a(self):
    #     assert demo("猴") == "孙悟空"
    #
    # def test_b(self):
    #     assert demo("猪") == "猪八戒"
    #
    # def test_c(self):
    #     assert demo("马") == "小白龙"

# 思考
# 正常情况下, 我们看到的是3个测试函数, 分别对应3条测试用例
# 用数据参数化的思维, 我们可以看到1个测试函数, 对应3条测试用例

    # @pytest.mark.parametrize("data", [["猴", "孙悟空"], ["猪", "猪八戒"], ["马", "小白龙"]])
    # def test_x(self, data):
    #     print(data, data[0], data[1])
    #     assert demo(data[0]) == data[1]

    # 优化
    l = [
        {"in": "猴","out": "孙悟空"},
        {"in": "猪","out": "猪八戒"},
        {"in": "马","out": "小白龙"}
    ]


    @pytest.mark.parametrize("data", l)
    def test_x(self,data):
        print(data, data["in"], data["out"])
        assert demo(data["in"]) == data["out"]