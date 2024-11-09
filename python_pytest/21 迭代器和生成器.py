# # 迭代器
# list1 = [1, 2, 3]
# # next(list1) # 会报错, 列表是可迭代对象, 但不是一个迭代器对象
#
# iter1 = iter(list1)     # 得到一个迭代器对象 iter
#
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))
# print(next(iter1))

# 生成器
# def gen():
#     for x in range(3):
#         yield x
#
#
# iter2 = gen()   # 生成器运行时会生成一个迭代器对象
# print(next(gen()))
# print(next(iter2))
# print(next(iter2))
# print(next(iter2))


# 这就是夹具的基本工作原理, 被夹的是测试函数
def gen():
    while True:
        print("我先干点啥")
        yield
        print("我再干点啥")


iter3 = gen()
next(iter3)
print("-------")
next(iter3)
print("-------")
next(iter3)

