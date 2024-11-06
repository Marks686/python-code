# break 作用是终止当前循环, 并跳出循环体外, 并继续执行循环之后的代码
# i = 1
# while i <= 5:
#     print(i)
#     if i == 3:
#         break
#     i += 1
#
# print(i)

# for x in "abcdefg":
#     print("前", x)
#     if x == "e":
#         break
#     print("后", x)
#
# print("最后", x)

# continue 的作用, 跳过本次循环中的剩余代码, 直接进入下一次循环
# i = 1
# while i <= 5:
#     print(i)
#     if i == 3:
#         continue    # 跳出本次循环导致 i += 1 未执行, 就会进入死循环
#     i += 1

# i = 1
# while i <= 5:
#     print(i)
#     i += 1
#     if i == 3:
#         continue

# for x in "abcdefg":
#     if x == "e":
#         continue
#     print(x)

# 注意点
# break和continue只能用在循环中, 除此之外不能单独使用
# break和continue在嵌套循环中, 只对最近的一层循环起作用

'''
python中如何跳出循环?[2]
- break, 用于结束循环
- continue, 用于跳出本次循环, 直接进入下一次循环
'''