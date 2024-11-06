'''
三大控制结构
python的三大控制结构分别是: 顺序, 分支, 循环, 用于控制代码的执行顺序
顺序: 从上而下, 顺序执行代码
分支: 根据条件判断, 确定执行哪个分支的代码
循环: 让特定代码块中的代码重复执行

while实现循环的基本语法

当 条件(满足时):
    要做的事
'''

# while True:
#     print("Hello World")

# 缺少条件限制, 会导致死循环
# i = 0
#
# while i < 5:
#     print("Hello World")
#     i = i + 1
#     print(i)

# i = 1
#
# while i <= 5:
#     print("Hello World")
#     i += 1
#     print(i)

# 计算1~100的累加和
# i = 1
# sum = 0
#
# while i <= 100:
#     sum += i
#     print("i目前的值是:", i)
#     print("sum目前的值是:", sum)
#     i += 1
#
# print(sum)

# 计算1~100的偶数的累加和
# i = 1
# sum = 0
#
# while i <= 100:
#     if i % 2 == 0:
#         sum += i
#     i += 1
#
# print(sum)

'''
while嵌套
和if嵌套类似, while嵌套就是while里面还有while

语法格式:

while 条件1:
    条件1满足时做的事
    
    while 条件2:
        条件2满足时做的事
'''
# 练习: 要求每天做3道题, 坚持7天
'''
while (天)条件:
    事
    while (题)条件:
        事
'''
day = 1
while day <= 7:
    problem = 1
    print("今天是第", day, "天")
    while problem <= 3:
        print("问题",problem)
        problem += 1
    day += 1






