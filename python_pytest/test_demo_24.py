from demo import demo


class TestDemo:

    def test_a(self):
        assert demo("猴") == "孙悟空"

    def test_b(self):
        assert demo("猪") == "猪八戒"

    def test_c(self):
        assert demo("马") == "小白龙"
