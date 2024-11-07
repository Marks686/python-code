# 什么是字典
# 字典 Dict, 语法上用 大括号 {} 来定义一个字典, 数据之间用 逗号 分隔
# 每个数据都是 键值对 的形式, 包含 键名(key) 和 键值(value) 两个部分
# d = {}
# print(type(d))
# t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}
# # 在字典中找到数据不是根据下标来找的, 是根据key
# print(t_info["name"])
# print(t_info["hobby"])

# 字典的常见操作
# 增, 使用 变量名["key"] = value 时, 如果 key 在字典中不存在, 就会新增这个数据
# t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}
# t_info["score"] = 10
# print(t_info)

# 删, pop 和 clear 方法
# t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}
# t_info.pop("age")
# print(t_info)
# t_info.clear()
# print(t_info)

# 改, 和新增一样, 使用 变量名["key"] = value 时, 如果 key 在字典中存在, 就会修改这个数据
# t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}
# t_info["age"] = 28
# print(t_info)

# 查
# t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}
# 查某个key对应的value
# print(t_info["name"])
# print(t_info.get("name"))
# # print(t_info["a"])      # key 不存在时会报错
# print(t_info.get("a"))    # key 不存在时会返回空值 None

# 查询字典的长度
# print(len(t_info))

# 查询字典中的key列表, value列表, 键值对元组的列表 (以前返回列表, 新版本python不再返回列表类型, 但可以当做列表来使用)
# t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}
# print(t_info.keys())
# print(list(t_info.keys()))
#
# print(t_info.values())
#
# print(t_info.items())

# 遍历
t_info = {"name": "杰哥", "sex": "男", "age": 18, "address": "广州", "hobby": ["吹牛", "看电影"]}

# for key in t_info.keys():
#     print(key)
#
# for value in t_info.values():
#     print(value)

for key, value in t_info.items():
    print(key, value)

'''
面试题
python中有哪些数据类型, 其中可变和不可变的数据类型有什么?[2]
- 常见的数据类型有: 整型 int, 浮点型 float, 布尔 bool, 字符串 str, 列表 list, 元组 tuple, 集合 set, 字典 dict
- 可变的数据类型有: 列表, 集合, 字典
- 不可变的数据类型有: 数字, 布尔, 字符串, 元组

python中的字典怎么遍历?[2]
- 字典类型有很多内置方法可以使用, 如: keys() 获取键列表, values() 获取值列表, items() 获取包含了键和值的元组的列表
- 有了这些可迭代的数据, 就可以通过 for 循环来遍历
'''





