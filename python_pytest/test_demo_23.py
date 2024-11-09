import pytest
from demo import demo

# 夹具的参数
# scope 作用域
    # function 函数级别, 默认值
    # class 类级别
    # module 模块级别
    # session [推荐]会话级别 (一次完整的自动化测试)
# autouse   自动使用
    # False 默认值, 代表不会自动使用
    # True 代表会自动使用 (意思是无需引用)

@pytest.fixture(scope="session", autouse=True)
def f():
    print("初始化")
    yield
    print("销毁资源")


class TestDemo:

    def test_a(self):
        assert demo("猴") == "孙悟空"

    def test_b(self):
        assert demo("猪") == "猪八戒"

    def test_c(self):
        assert demo("马") == "小白龙"
