import pytest
from demo import demo


class TestDemo:

    def test_a(self):
        assert demo("猴") == "孙悟空"

    def test_b(self):
        assert demo("猪") == "猪八戒"

    def test_c(self):
        assert demo("马") == "小白龙"

    def test_d(self):
        assert 2 != 1

    @pytest.mark.xfail
    def test_e(self):
        assert 2 > 1

    @pytest.mark.skipif(condition=True, reason="我就是要跳")
    def test_f(self):
        assert "hello" in "hello world"

    @pytest.mark.skip
    def test_g(self):
        assert isinstance(1, int)

    @pytest.mark.xfail
    def test_h(self):
        assert False    # 加了预期失败的装饰器 属于 Expected failures, 就不是 Failed 的情况了
