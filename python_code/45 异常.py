# s = "123"
# del s[0]    # 对于不可变数据类型, 这样删除元素会报错 TypeError

# info = {"name": "杰哥"}
# info["age"]     # 字典引用不存在的键会报错 KeyError

# open("12345.txt")   # 打开文件, 文件不存在会报错 FileNotFoundError
# 什么是异常
# 程序在运行时, 如果python解释器遇到了一个错误, 会停止程序的运行, 并提示错误信息
# 这些错误信息就是异常
# 提示错误信息的动作就是抛出异常 (当然直接叫提示错误信息或报错都可以)
# 正确的认识异常
    # 异常并不可怕, 软件是给用户群体使用的, 所谓异常, 只不过是一个很普通的用户场景
    # 可怕的是异常会停止程序的运行

# 捕获异常-处理异常
# 当我们不确定某些代码能不能执行成功时, 可以用如下语法来避免程序停止运行:
# try:
#     尝试执行的代码
# except:
#     出现错误的处理代码

# 示例
# try:
#     open("12345.txt")
# except:
#     print(1)
#
# print(2)

# 如果希望能够显示异常信息, 如何处理
# try:
#     open("12345.txt")
# except FileNotFoundError as e:
#     print(e)
#     print(1)
#
# print(2)

# 如果不知道异常的类型怎么办? (通过异常类的继承关系寻找)
# Exception 是所有内置标准异常的基类(父类)
# BaseException 是所有内置+自定义异常的基类

# try:
#     open("12345.txt")
# except BaseException as e:
#     print(e)
#     print(1)
#
# print(2)

# 优雅的解决方案
# try:
#     # 让用户尝试输入密码并登录的代码
# except 密码为空的错误类型 as e:
#     print(e)
#     # 让用户记得要输入密码的代码
# except 密码错误的异常类型 as e:
#     print(e)
#     # 让用户再次尝试输入密码的代码
# except BaseException as e:
#     print(e)
#     # 鬼知道用户弄出了什么幺蛾子的处理代码
# else:
#     # 没有异常才会执行的代码
# finally:
#     # 无论是否有异常, 都会执行的代码

# 异常的实际应用[了解]: 设计一个 8/x 的程序, x来自于用户输入

# try:
#     num = int(input("请输入一个整数: "))
#     result = 8/num
#     print(result)
# except ZeroDivisionError as e:
#     print(e)
#     print("小学数学是体育老师教的吧, 0不能做除数")
# except ValueError as e:
#     print(e)
#     print("别捣蛋, 要整数, 整数, 整数")
# except BaseException as e:
#     print(e)
#     print("未知错误")
# else:
#     print("正常执行")
# finally:
#     print("finally, 不管有没有异常, 反正都要说一句")

'''
面试题
如何捕捉一个异常?[1]
可以使用try...except...语法来捕捉异常, 如果后续有需要执行的代码可以放在 finally 代码块中
'''

# 以上都是程序运行过程中遇到错误的情况, 能不能手动抛出一个异常[了解]
vx_list = ["张三", "李四", "王五", "情敌"]

# for friend in vx_list:
#     print(friend)
#     if friend == "情敌":
#         raise Exception("我很生气")

class VeryAngryException(BaseException):
    pass

for friend in vx_list:
    print(friend)
    if friend == "情敌":
        raise VeryAngryException("我很生气")