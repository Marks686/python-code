import pytest

# if __name__ == "__main__" 用于运行环境检测
# __name__ 是一个内置变量, 当文件被运行时 __name__ 被设置为 "__main__",
# 当被导入到其他文件时, 则判断条件不成立
if __name__ == "__main__":
    pytest.main(['-vs', 'test_demo_11.py'])


