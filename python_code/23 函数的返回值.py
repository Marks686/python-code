# 什么是返回值
# 在程序开发中, 有时候会希望一个函数执行结束后, 告诉调用者一个结果, 这个结果就是返回值
# 语法上, 使用 return 这个关键字来返回结果
# def add(x, y):
#     print(x + y)
#
# a = add(1, 2)
# print(a)    # 结果是None, 说明add函数只关注打印的过程, 没有返回值

# def add(x, y):
#     return x + y
#
# a = add(1, 2)
# print(a)
# print(add(1, 2))

# 注意: 函数执行到了return就好结束
def demo():
    print(1)
    print(2)
    return 0
    print(3)
    print(4)

demo()