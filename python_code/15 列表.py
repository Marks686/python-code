# 列表(中的数据)常见的增删改查等操作
# 增: append, extend, insert
# append 可以把数据加到列表的末尾
# l = [1, 2]
# l.append(3)
# l.append("a")
# l.append(True)
# l.append([5, 6])
# print(l)

# extend 可以把一个可迭代类型数据中的元素逐一加到列表中
# a = [1, 2]
# b = [3, 4]
# c = "abc"
# a.extend(b)
# a.extend(c)
# print(a)

# insert 可以在指定位置前插入数据
# l = [1, 2, 3, 4]
# l.insert(2, "a")
# print(l)

# 删: pop, remove
# pop 根据索引删除列表中的数据, 默认删除列表中的最后一个数据
# l = [1, 2, 3, 4]
# # l.pop()
# l.pop()
# # l.pop(2)
# print(l)

# remove 根据值从列表中删除数据
# l = [1, 2, 3, 4]
# l.remove(3)
# ll = ["张三", "李四", "王五"]
# ll.remove("李四")
# print(ll)
# print(l)

# 改, 修改列表中的数据有很多方法, 需要灵活运用, 最常见的是根据下标进行数据的修改
# l = [1, 2, 3, 4]
# l[1] = 3
# print(l)

# 查
# in 和 not in 用于判断列表中是否存在某数据, 成功为True, 失败为False
# l = [1, 2, 3, 4]
# if 1 in l:
#     print("存在")
# if "a" in l:
#     print("存在")
# if 6 not in l:
#     print("不存在")

# index 和 count
l = [1, 2, 2, 4]
print(l.index(1))
print(l.count(1))
print(l.index(2))
print(l.count(2))





