import pytest


class TestLogin:

    def test_a(self):
        print("test_a")

    def test_b(self):
        print("test_b")

if __name__ == '__main__':
    pytest.main(["-s", "test_duanyan.py"])
# 主函数运行方式需要先导包 import pytest

