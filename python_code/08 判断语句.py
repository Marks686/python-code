'''
抽象出来的基本逻辑如下:

如果 判断条件:
    (条件成立时)做这些事
否则:
    做其他事

语法格式
if 条件:
    事
'''
# # age = 19
# age = 17
#
# if age >= 18:
#     print("可以去网吧上网")

'''
if else
语法格式
if 条件:
    条件满足时的事
else:
    不满足条件时要做的事儿
'''
# age = 19
#
# if age >= 18:
#     print("可以去网吧上网")
# else:
#     print("不能去网吧上网")
#     print("只能回家")

# 练习: 获取用户输入的年龄, 判断是否满足18岁, 如果满足, 则打印1, 不满足, 则打印2
'''
其实if else语法组合就是我们常说的分支结构, 分支有几条? 可以增加分支吗? 答案就是 elif
语法格式:

if 条件1:
    事情1
elif 条件2:
    事情2
elif 条件3:
    事情3
else:
    事情4

说明
如果满足条件1, 执行事情1, 代码块执行结束
否则, 如果满足条件2, 执行事情2, 代码块执行结束
否则, 如果满足条件3, 执行事情3, 代码块执行结束
否则, 执行事情4, 代码块结束
'''
# score = 62
#
# if 90 <= score <= 100:
#     print("本次考试成绩为A")
# elif 80 <= score < 90:
#     print("本次考试成绩为B")
# elif 70 <= score < 80:
#     print("本次考试成绩为C")
# elif 60 <= score < 70:
#     print("本次考试成绩为D")
# else:
#     print("本次考试成绩不及格")

# if嵌套[了解]
# a = "帅"
# b = "善良"
# c = "有腹肌"
#
# if a == "帅":
#     if b == "善良":
#         if c == "有腹肌":
#             print("处对象")

# match...case..., python3.10以上版本的新特性, 也属于分支结构的一种
x = 4

match x:
    case 1:
        print("x is 1")
    case 2:
        print("x is 2")
    case 3:
        print("x is 3")














