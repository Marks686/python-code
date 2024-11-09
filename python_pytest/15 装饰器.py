# def hello():
#     print("hello")
#
#
# # 先解决第一个问题, 函数名也可以作为输入
# def world(func):
#     func()
#     print("world")
#
#
# world(hello)

import time


# # 如果要给hello函数加上延时3s执行的功能
def hello():
    time.sleep(3)   # 不使用装饰器, 内部修改不是动态的, 且不通用
    print("hello")

hello()

# 装饰器的语法
# def 装饰器函数名(输入函数名):
#     def 内部函数名(参数):
#         先干点啥
#         result = 输入函数名(参数)
#         再干点啥
#         return result
#     return 内部函数名

# 可以写一个装饰器函数, 功能是延时3s执行
def time_delay(func):
    def inner():
        time.sleep(3)
        result = func()
        return result
    return inner

# 再写一个装饰器函数, 功能是重复n次
def repeat(n):
    def outer(func):
        def inner():
            for i in range(n):
                result = func()
            return result
        return inner
    return outer

# 使用 @ 符号来表示使用装饰器
# @time_delay
@repeat(200)
def hello():
    print("hello")

hello()
