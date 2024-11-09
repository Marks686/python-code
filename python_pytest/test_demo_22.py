import pytest
from demo import demo


@pytest.fixture()
def f():
    print("初始化")
    yield
    print("销毁资源")


class TestDemo:

    def test_a(self, f):    # 夹具引用方法1: 通过参数引用
        print("1")      # 证明被夹了
        assert demo("猴") == "孙悟空"

    @pytest.mark.usefixtures("f")   # 夹具引用方法2: 通过装饰器引用夹具
    def test_b(self):
        assert demo("猪") == "猪八戒"

    def test_c(self):
        assert demo("马") == "小白龙"
