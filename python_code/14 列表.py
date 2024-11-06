# 什么是列表
# 列表 List 是python中使用非常频繁的数据类型, 在其他语音中通常叫做 数组
# 语法上用 [] 来定义一个列表, 数据之间用 逗号 分割, 例如
# name_list = ["张三", "李四", "王五"]
# 列表的索引从0开始(索引就是下标), 引用超出索引范围会报错
# print(name_list[0])
# print(name_list[2])
# print(name_list[3])
# 列表可以储存不同类型的数据
l = ["张三", 100, [1, 2]]
print(l[0])
print(l[1])
print(l[2][1])

# # 列表的遍历
# name_list = ["张三", "李四", "王五"]
#
# # for
# for name in name_list:
#     print(name)
#
# # while
# i = 0
# while i < len(name_list):
#     print(name_list[i])
#     i += 1