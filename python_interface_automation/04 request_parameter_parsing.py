import requests

### 请求参数解析
kw = {
    "method":"xx",
    "url":"xx",
    "params": None,
    "data":None,
    "json":None,
    "files":None,
    "headers": None
}

# 定义各个接口对应的数据为
kw1 = {
    "method":"get",
    "url":"http://127.0.0.1:1234/area/listarea",
    "params": None,
    "data":None,
    "json":None,
    "files":None,
    "headers": None
}

# 查单个信息
kw2 = {
    "method":"get",
    "url":"http://127.0.0.1:1234/area/getareabyid",
    "params": {"areaId":1},
    "data":None,
    "json":None,
    "files":None,
    "headers": None
}

# 新增区域
kw3 = {
    "method":"post",
    "url":"http://127.0.0.1:1234/area/addarea",
    "params": None,
    "data":{"areaName":"一灯","priority":"100"},
    "json":None,
    "files":None,
    "headers": None
}
# 修改区域
kw4 = {
    "method":"put",
    "url":"http://127.0.0.1:1234/area/modifyarea",
    "params": None,
    "data":None,
    "json":{"areaId":67,"areaName":"段智兴","priority":"100"},
    "files":None,
    "headers": None
}
# 删除区域
kw5 = {
    "method":"delete",
    "url":"http://127.0.0.1:1234/area/removearea",
    "params": {"areaId":67},
    "data":None,
    "json":None,
    "files":None,
    "headers": None
}
response = requests.request(**kw4)

print("状态码：",response.status_code)
print("响应体：",response.text)