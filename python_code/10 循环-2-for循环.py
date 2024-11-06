# python 中的 for 循环, 可以遍历任何可迭代对象, 如: 字符串, 列表, 元组, 字典
# 遍历可迭代对象: 指按顺序, 逐一得到全部数据, 且无遗漏
'''
语法格式

for 临时变量 in 可迭代对象:
    满足条件时执行的代码
'''
# for x in "123456789":
#     print(x)

# 如果需要循环100次怎么办?
for i in range(12):
    print(i)


# a = range(5)
# b = list(a)
# print(b)



# 效果等同于
# i = 0
# while i < 100:
#     print(i)
#     i += 1

# range() 函数返回一个可迭代对象(类型是对象),打印时不能直观看到数据
# 可以通过 list() 函数可以把可迭代对象转为一个列表
# a = range(5)
# print(list(a))

