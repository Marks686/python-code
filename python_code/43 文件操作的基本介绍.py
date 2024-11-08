# 文件的基本认知
# 计算机的文件, 本质上就是长期存储设备上的一段数据 (长期存储设备包括光盘/U盘/硬盘, 但不包括内存)
# 在计算机中, 文件是以二进制的方式保存在硬盘上
    # 文本文件, 本质上依然是二进制文件 (字符编码), 只不过查看时进行了解码, 让二进制重新转为自然语言

# 文件的基本操作
# 基本操作包括的范围: 1.打开文件 2.读写文件 3.关闭文件
# 对读写的理解
    # 读, 将文件内容读入内存, 可以理解为查看文件内容
    # 写, 讲内存内容写入文件, 可以理解为增/删/改文件内容并保存

# 打开文件 open 和 关闭文件 close
# open("test.txt")  直接运行会报错, 意思就是这个文件不存在
# open(文件名, 访问模式) 用于打开一个文件, 返回这个文件对象, 访问模式介绍如下:
# r 以只读方式打开文件(默认访问模式)
# w 打开一个文件用于写入, 会覆盖写入, 如文件不存在则创建
# a 打开一个文件用于写入, 会追加写入, 如文件不存在则创建
# b 二进制模式, 使用时结合其他模式: rb, wb, ab
# f = open("test.txt", "w")
# f.write("2222")

f = open("test.txt", "a")
f.write("1")

# f = open("test.txt", "ab")
# f.write("1".encode("utf8"))
#
f.close()

# 读写文件: read, write
# 使用 write() 方法可以向文件写入数据
# f = open("test.txt", "a")
# f.write("1")
# f.write("2\n")
# f.close()

# 使用 read(n) 方法可以从文件读取 n个字符的数据
# f = open("test.txt", "r")
# print(f.read(5))    # 从头读5个字符
# print(f.read(5))    # 接着再读5个字符
# print(f.read())     # 读取剩余全部
# # 说明: 其实文件操作存在一个叫做文件指针的概念, 类似光标, 它标记着操作文件的位置
#
# f.close()

# 注意编码问题, 如: 文件内容中包含汉字时, 读文件时容易出现编码错误
# f = open("test.txt", "r", encoding="utf8")
# print(f.read())
# f.close()

# 文件内容较多时, 可以逐行读取
# f = open("test.txt", "r", encoding="utf8")
# print(f.readline()) # 行尾有换行符, print也有换行符
# print(f.readline())
#
# f.close()

# 比较优雅的写法
# f = open("test.txt", "r", encoding="utf8")
# for line in f.readlines():
#     print(line, end="")
#
# f.close()

# 如果总是忘记close怎么办[拓展]
# with 语句可以优雅的处理资源管理问题
# with open("test.txt", "r", encoding="utf8") as f:
#     pass

# 其中 with open("test.txt", "r", encoding="utf8") as f:
# 相当于 f = open("test.txt", "r", encoding="utf8") 加上 f.close()










