# 匿名函数的定义语法是 lambda 参数: 表达式
# 匿名函数中不能使用 print, 表达式就是返回值 (无需写 return)
# def sum1(x, y):
#     return x + y
#
# print(sum1(1, 2))
# # 应用1
# sum2 = lambda x, y: x + y
# print(sum2(2, 3))

# 应用2, 在高阶函数中, 作为参数传递
def sq(x):
    return x**2


print(list(map(sq, [x for x in range(10)])))

print(list(map(lambda x: x**2, [x for x in range(10)])))