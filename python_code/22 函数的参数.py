# def add_2num():
#     x = 1
#     y = 2
#     print(x + y)
#
# add_2num()
# 这个函数只能把固定的两个数想加, 怎么样让这个函数适用于可变的两个数相加, 答案就是参数
# def add(x, y):
#     print(x + y)
#
# add(2, 3)

# 参数的基本含义
# 形参: 在定义时使用, 用于在调用时接收变量值的形式参数 (如, 上述代码中的 x 和 y)
# 实参: 在调用时传入的实际参数值 (如, 上述代码中的 2 和 3)

# 注意, 在调用函数时, 参数的位置和数量要保持一致
# def add(x, y):
#     print(x + y)

# add(1, 2, 3)    # 参数数量不一致会报错
# add(y=1, x=2)   # 如果位置需要变动, 则需要以 变量名=参数值 的形式传参

# 参数的默认值(缺省值), 需保证带有默认值的参数在末尾 def add(x=1, y): 是错误的
# def add(x, y=1):
#     print(x + y)
#
# add(2, 2)
# add(1)

# 参数[拓展]
# def len(*args, **kwargs): 在这个定义中 *args, **kwargs 是什么?
# 这些用于传参数量不确定的情况

# *args 用于接收不确定个数的参数, 它会将传入的参数打包成一个元组
# def demo(*args):
#     print(args)
#
# demo(1, 2, 3)

# **kwargs 用于接收不确定个数的关键字参数(键=值), 并打包成一个字典
# def demo(**kwargs):
#     print(kwargs)
#
# demo(a=1, b=2, c=3)

# 说明
# args 和 kwargs 是可以改变名字的, 但不推荐
# args 是 arguments (参数) 的缩写
# kw 是 keyword (关键字) 的缩写
# 参数定义是有顺序的: 必选参数, 默认参数, 可变参数, 如:
# def demo(a, b, c=1, *args, **kwargs):
#     print(a)
#     print(b)
#     print(c)
#     print(args)
#     print(kwargs)
#
# demo(1, 2, 3, 4, 5, 6, aa=7, bb=8, cc=9)

# 练习: 计算任意多个数字的和
def sum_num(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)

sum_num(1, 2, 3, 4, 5, 6, 7, 8, 9)

'''
面试题
python的函数怎么传入可变参数 或 传参时的 * 和 ** 是什么意思?[1]
- 设计函数时, 如果不确定参数的个数, 这个时候我们就需要传入可变参数
- * 用于接收不确定个数的参数, 并打包成一个元组, 定义形参时通常用 *args
- ** 用于接收不确定个数的关键字参数, 并打包成一个字典, 定义形参时通常用 **kwargs
'''








