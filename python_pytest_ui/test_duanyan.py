def add(x, y):
    return x + y

class TestPlus:

    # 判断 1+1 的结果等于 2
    def test_a(self):
        assert 2 == add(1, 1)

    # 调换表达式两个值的位置, 判断 1+1 的结果等于 2
    def test_b(self):
        assert add(1, 1) == 2

    # 判断 1+2 的结果不等于4
    def test_c(self):
        assert 4 != add(1, 2)

    # 误判: 1+2 等于 4 了
    def test_d(self):
        assert 4 == add(1, 2)