# 除了文件的打开/关闭, 读/写外, 对文件还有重命名, 删除等操作, 甚至对文件夹也有增删改查等操作, 如何实现?
# 这些功能都在 python 的 os 模块中
# 学习相关操作之前, 需要先了解模块和包

# 什么是模块, 什么是包
# - 把功能相关的函数/类放在一个独立的 py 文件中, 就形成了一个模块
# - 把功能相关的模块整理放到一个独立的文件夹中, 就形成了一个包
# - 一个模块就是一个 py 文件, 一个包就是一个包含了 __init__.py 文件的文件夹

# 如何导入封装好的模块, 包

# 从结构上认清我们要导入的内容
# 项目1
#     包1
#         模块1
#             类1, 方法1, 函数1, 变量1, ...
#         模块2
#     包2

# 使用 import 来导入模块和模块中定义的类/方法/函数/变量
# import math
#
# print(math.pi)
# print(math.sqrt(2)) # sqrt 平方根函数

# 如果想直接使用模块中的成员, 不想以 模块.成员 的方式来使用
# from math import pi, sqrt
# from math import *
#
# print(pi)
# print(sqrt(2))

# as 给导入的对象取别名
# from math import pi as PI
# print(PI)   # 此时 pi 就只能通过别名来使用了
#
# import time as t
# t.sleep(3)

# 语法小结, 下面几种情况, 后面都可以加 as 来取别名
# import 模块名
# from 模块名 import 成员名
# from 包名.模块名 import 成员名

# 模块和包的基本使用示例
# 同一个目录下, 存在两个模块 a 和 b, 需要在 b 中调用 a 模块的函数或方法
# 在 a.py 中写一个函数和一个类
# def add(x, y):
#     return x + y
#
# class Dog:
#
#     def eat(self):
#         print("chua chua chua~")

# 在 b.py 中如果要使用a 模块中的函数或方法, 可以使用 Alt + 回车 来自动导入
# from a import add, Dog
#
# print(add(1, 2))
#
# dog = Dog()
# dog.eat()

# 也可以手动导入模块 a
# import a
#
# print(a.add(1, 2))
#
# dog = a.Dog()
# dog.eat()

# 如果 a和b两个模块存在于不同的包里面, 还需要在b 模块中调用a模块, 改如何操作
# A包内有a模块, B包内有b模块
# from A.a import add
#
# print(add(1, 2))

# os模块的文件相关操作
import os

# 文件重命名
# os.rename("test.txt", "test1.txt")

# 删除文件
# os.remove("test1.txt")

# 创建文件夹
# os.mkdir("abc")

# 获取当前目录
# print(os.getcwd())

# 删除目录
# os.rmdir("abc")


