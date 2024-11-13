import pytest


class TestDemo:

# 需求: 不使用数据参数化, 分别打印用户名 "zhangsan" 和 "lisi"
    def test_a(self):
        print("zhangsan")

    def test_b(self):
        print("lisi")

# 需求: 使用数据参数化 (单一参数), 修改上面的代码
    @pytest.mark.parametrize("name", ["zhangsan", "lisi"])
    def test_c(self, name):
        print(name)