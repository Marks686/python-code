### 登录session
import requests

# TPshop 获取验证码 + 个人信息接口
# 初始化数据
code = {"method": "get", "url": "http://192.168.10.139/index.php?m=Home&c=User&a=verify"}
login = {
    "method": "post",
    "url": "http://192.168.10.139/index.php?m=Home&c=User&a=do_login",
    "data": {"username": "15249205917", "password": "123456", "verify_code": "8888"}}
info = {"method": "get", "url": "http://192.168.10.139/index.php/Home/User/info.html"}

# 创建session对象
session = requests.Session()


# 1.获取验证码，并获取cookie，并装进session对象
res1 = session.request(**code)

# 2.发送登录请求
res2 = session.request(**login)
print(res2.text.encode("utf-8").decode("unicode_escape"))

# 3.发送个人信息请求
res3 = session.request(**info)
print(res3.text)