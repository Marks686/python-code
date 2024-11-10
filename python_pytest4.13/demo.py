# 解决 2.部分字符串的值需变为字典 问题
# 需要用到 eval() 它可以将 str 当成有效的表达式求值并返回计算结果
# 此处我们使用 eval() 的目的是, 把 str 转换成 dict, (当然也可以把 str 转换成 list, tuple 等)
s1 = "len('hello')"
print(s1)
print(eval(s1))

s2 = '{"name": "zhangsan", "age": len("0000000000")}'
print(s2, type(s2))
print(eval(s2), type(eval(s2)))

# 使用时一定要注意 eval() 的参数必须传, 且必须 str, 如果传入空(None)会报错
# 逻辑需要处理为
# if isinstance(case["headers"], str):
#     hearders = eval(case["headers"])
# else:
#     hearders = None

# 简单的写法为 hearders = eval(case["headers"]) if isinstance(case["headers"], str) else None
