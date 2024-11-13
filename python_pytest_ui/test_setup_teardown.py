import time


def add(x, y):
    return x + y

class TestPlus:

    # 获取并打印开始时间, 每个测试函数执行前都打印一次
    def setup(self):
        print("start-time:", time.time())

    # 获取并打印结束时间, 每个测试函数执行后都打印一次
    def teardown(self):
        print("end-time:", time.time())

    def test_a(self):
        assert 2 == add(1, 1)

    def test_b(self):
        assert add(1, 1) == 2
