import json

# 读取 data.json 文件
with open("data.json", "r", encoding="utf-8") as f:
    data1 = json.load(f)
    print(data1)

# 把字典写入json文件 "data2.json"
data2 = data1
with open("data2.json", "w", encoding="utf-8") as f:
    json.dump(data2, f)

# 把字典写入json文件 "data3.json"  ------解决写入中文的问题
data3 = data1
with open("data3.json", "w", encoding="utf-8") as f:
    json.dump(data2, f, ensure_ascii=False)

