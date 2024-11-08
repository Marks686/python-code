### 登录-cookie
# TPshop 获取验证码 + 个人信息接口
import requests

# TPshop 获取验证码 + 个人信息接口

code = {"method": "get", "url": "http://192.168.10.139/index.php?m=Home&c=User&a=verify"}
login = {
    "method": "post",
    "url": "http://192.168.10.139/index.php?m=Home&c=User&a=do_login",
    "data": {"username": "15249205917", "password": "123456", "verify_code": "8888"},
    'cookies': None
}
info = {"method": "get", "url": "http://192.168.10.139/index.php/Home/User/info.html"}

# 1. 获取验证码,并获取cookie
res1 = requests.request(**code)
print(res1.cookies.get("PHPSESSID"))

# 2.登录，并提交 cookie
login['cookies'] = {"PHPSESSID": res1.cookies.get("PHPSESSID")}
res2 = requests.request(**login)
print(res2.text.encode("utf-8").decode("unicode_escape"))
# 3. 获取个人信息
info['cookies'] = {"PHPSESSID": res1.cookies.get("PHPSESSID")}
res3 = requests.request(**info)
print(res3.text)