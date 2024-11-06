# 排序
# sort方法是将列表按顺序重新排列, 默认为从小到大, 参数 reverse=True 则是倒序
# l = [1, 3, 4, 2]
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# ll = ["b", "c", "a"]
# ll.sort()
# print(ll)
# 注意: 列表中的数据需要是同一类型的, 同时存在数字和字符串就不能排序

# # [了解]列表生成式, 顾名思义, 可以帮我们生成列表
# # 生成0~9的10个数
# a = [x for x in range(10)]
# print(a)

# # 生成1~10
# b = [x for x in range(1, 11)]   # 可以按住 ctrl + 鼠标左键, 进入一个函数
# print(b)

# # 生成10以内的奇数/偶数
# c = [x for x in range(1, 11) if x % 2 == 1]
# d = [x for x in range(1, 11) if x % 2 == 0]
# print(c)
# print(d)

# # 生成10以内的各数的平方
# e = [x**2 for x in range(1, 11)]
# print(e)

'''
面试题
列表中的数据如何拼接成字符串?[1]
- 想把列表中的元素拼接成一个字符串有很多方法
- 其一, 我们可以使用 join 方法, 用空字符串做分隔符来连接列表中的元素
- 其二, 我们可以使用 + 运算符, 循环向空字符串中逐一添加列表中的元素
'''
name_list = ["张三", "李四", "王五"]
#
# # 使用 + 运算的方法
s = ""
for name in name_list:
    s = name + s
print(s)
# # 使用join, 用于将列表中的数据以某个分隔符进行连接, 返回字符串
result = "".join(name_list)
print(result)
