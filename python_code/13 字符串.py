# 字符串常见操作
# len(), 获取字符串长度
# s = "听君一席话,如听一席话"
# print(len(s))

# find() 和 index(), 检测字符串中是否包含某个子串
# 如果包含, 则返回第一个找到的子串的初始下标
# s = "听君一席话,如听一席话"
# print(s.find(","))
# print(s.index(","))
# 区别在于, 如果找不到, find返回-1, index则抛出异常
# print(s.find("二"))
# print(s.index("二"))

# [了解] s.find(sub, start, end)
# start 表示搜索的起始位置, 默认为0 [可选]
# end 表示搜索的结束位置, 默认为字符串的长度 [可选]
# index() 也支持这种写法
# print(s.find("一席话", 0, 11))
# print(s.find("一席话", 6, 11))

# replace(), 替换字符串中的某些子串, 可以控制替换次数
# s = "听君一席话,如听一席话"
# print(s.replace("一", "二"))
# print(s.replace("一", "二", 1))

# count(), 返回字符串中某个子串出现的次数
# s = "听君一席话,如听一席话"
# print(s.count("一席话"))
# print(s.count("一席话", 6, 11))

# split(), 以某字符为分隔符进行切片
# s = "听君一席话,如听一席话"
# print(s.split("一"))

# startwith() 和 endwith(), 检查字符串是否以某子串为开始或结束, 是则True, 否则False
# s = "听君一席话,如听一席话"
# print(s.startswith("听"))
# print(s.startswith("一"))
# print(s.endswith("一"))
# print(s.endswith("如听一席话"))

# lower() 和 upper(),把字符串中的所有字符转为小写 或 大写
# s = "Hello World"
# print(s.lower())
# print(s.upper())

# isalpha(), isdigit() 和 isalnum(),判断字符中所有字符都是 字母, 数字, 字母或数字
# 是则True, 否则False
# s1 = "helloworld"
# s2 = "123"
# s3 = "helloworld123"
# print(s1.isalpha())
# print(s2.isdigit())
# print(s3.isalnum())

# join(), 格式为 分隔符.join(数据), 数据可以是字符串, 列表, 元组, 字典, 返回值是字符串
# s = "听君一席话,如听一席话"
# print("666".join(s))

# l = ["广东省", "广州市", "天河区..."]
# print(l)
# print("  ".join(l))

'''
如何实现字符串的反转?[2]
实现字符串反转的方法很多, 比如切片, 内置函数, 循环等
- 切片的方式最方便, 只需要设置步长为-1即可
- 内置函数的方法思路是先用reversed函数反转, 再用join函数进行拼接
- 循环的方法思路是遍历字符串的每个字符, 循环拼接时, 用 新字符+旧字符 的方式就可以得到结果
'''
s = "abcde"
# 切片
print(s[::-1])

# 内置函数 reversed 返回逆序迭代器, 使用 join 进行拼接
print("".join(reversed(s)))

# 循环
ss = ""         # 定义一个空字符串
for c in s:
    ss = c + ss  # 每次循环新拿出的字符c, 排在前面
print(ss)