# 什么是字符串
# 双引号或者单引号中的数据就是字符串
# a = "abc"
# b = '1232131'
# c = '{[(1232131)]}!@#$%^^&&'
# d = "      @_@     震惊"
#
# print(type(d))

# 电子生日贺卡中的祝福语, "Hello xx, 祝你 xx 岁生日快乐!"
# name = "张三"
# age = 18
# print("Hello", name, ", 祝你", age, "岁生日快乐!")

# 字符串格式化
# 就是把变量嵌入到字符串中, 推荐 字符串.format()
# print("Hello {}, 祝你 {} 岁生日快乐!".format(name, age))

# 自定义名片
# name = input("请输入你的名字: ")
# position = input("请输入你的职位: ")
# company_name = input("请输入你的公司名称: ")
#
# print("-" * 30)
# print("姓名: {}".format(name))
# print("职位: {}".format(position))
# print("公司名称: {}".format(company_name))
# print("-" * 30)

# 字符串的下标
# 下标其实就是编号, 比如高铁上的座位号, 超市储物柜的编号, 用 字符串[下标], 如 "abc"[1]
s = "abcdef"

# 下标从左往右, 从0开始
# print(s[0])
# print(s[2])
# print(s[5])
# print(s[6]) # 超出下标范围会报错
# print("aabbcc"[4])

# 还有一套下标是从右往左, 从-1开始
# print(s[-6])
# print(s[-1])

# 切片: 指截取其中一部分, 字符串/元组/列表都支持切片
# 语法: [起始下标:结束下标:步长]
# 从起始位开始, 到结束位为止(不包含结束位本身), 步长表示切片间隔
s = "abcdefgh"
# print(s[:])     # 取所有, 默认步长为1
# print(s[::2])   # 取所有, 默认步长为2
# print(s[:3])    # 取前3位
# print(s[5:])    # 取第5位以后的内容
# print(s[1:5])   # 取第2, 3, 4, 5位的内容
# print(s[1:5:2]) # 取第2, 4位的内容
# print(s[1:-1])  # 取第2位到倒数第2位的内容
# print(s[5:1:-2])   # 步长是负数, 表示反向(从右向左), 取第6位和第4位
# print(s[::-1])  # 反转字符串
# print(s[-1::-1])
# print(s[7::-1])





















