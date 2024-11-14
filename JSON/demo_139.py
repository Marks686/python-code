import json

# 把python字典类型转换为JSON字符串
dict1 = {
    "name": "zhangsan",
    "age": 18,
    "is_man": True,
    "school": None
}
# 使用 dumps 方法, 得到的结果是 json 字符串
json_str1 = json.dumps(dict1)
print(json_str1)

# 把JSON字符串转换为python字典
json_str2 = '{"name": "zhangsan", "age": 18, "is_man": true, "school": null}'
# 使用 loads 方法, 得到的结果是 python字典
dict2 = json.loads(json_str2)
print(dict2)