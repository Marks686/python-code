import pytest
from demo import demo


class TestDemo:

    @pytest.mark.run(order=1)
    def test_a(self):
        assert demo("猴") == "孙悟空"

    @pytest.mark.run(order=-1)
    def test_b(self):
        assert demo("猪") == "猪八戒"

    @pytest.mark.run(order=2)
    def test_c(self):
        assert demo("马") == "小白龙"

    @pytest.mark.run(order=-2)
    def test_d(self):
        assert 2 != 1

    @pytest.mark.run(order=0)
    def test_e(self):
        assert 2 > 1

    @pytest.mark.run(order=1.5)
    def test_f(self):
        assert "hello" in "hello world"

    def test_g(self):
        assert isinstance(1, int)

    def test_h(self):
        assert True


