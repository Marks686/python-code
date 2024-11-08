import requests

### 实现HTTP请求
# 查询全部区域信息
# VM service_api 这个虚拟机的地址
# response = requests.get("http://192.168.10.131:1234/area/listarea")
# 本地
# response = requests.get("http://127.0.0.1:1234/area/listarea")
# 带参数的get请求
# response = requests.get("http://127.0.0.1:1234/area/getareabyid?areaId=1")
# 带参数的get请求
# response = requests.get("http://127.0.0.1:1234/area/getareabyid",params={"areaId":1})
# 新增区域
# response = requests.post("http://127.0.0.1:1234/area/addarea",data={"areaName":"杨过","priority":90})
# 修改区域
# response = requests.put("http://127.0.0.1:1234/area/modifyarea",
#                         json={"areaId":2,"areaName":"甄志丙","priority":100})
# 删除区域
response = requests.delete("http://127.0.0.1:1234/area/removearea",params={"areaId":2})

# 打印结果
print("状态码：",response.status_code)
print("响应体：",response.text)