import requests
import jsonpath

login = {
    "method":"post",
    "url":"http://192.168.10.131:8888/api/private/v1/login",
    "params": None,
    "data": {"username":"admin","password":"123456"},
    "json":None,
    "files":None,
    "headers": None
}
user_list = {
    "method":"get",
    "url":"http://192.168.10.131:8888/api/private/v1/users",
    "params": {"pagenum": 1,"pagesize": 1},
    "data":None,
    "json":None,
    "files":None,
    "headers": None
}

# 1。登录
res1 = requests.request(**login)
print(res1.json())
# 2. 提取token
    # 方法1：
# token = res1.json()["data"]["token"]
    # 方法2：jsonpath
token = jsonpath.jsonpath(res1.json(),"$..token")[0]
# print(token)
# 3.获取用户数据列表
user_list['headers'] = {"Authorization": token}
res2 = requests.request(**user_list)
print(res2.json())