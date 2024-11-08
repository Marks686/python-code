### 接收响应结果
import requests

kw1 = {
    "method":"get",
    "url":"http://127.0.0.1:1234/area/listarea",
    "params": None,
    "data":None,
    "json":None,
    "files":None,
    "headers": None
}
response = requests.request(**kw1)


# 行解析
print("URL：",response.url)
print("状态码：",response.status_code)

# 头解析
print("响应头：",response.headers)
# headers中指定的信息
print("响应头中的Content-Type：",response.headers.get("Content-Type"))
# cookies解析
print("cookies信息：",response.cookies)
# 遍历cookies
# for name,value in response.cookies.items():
#     print(name,value)
# 体解析
print("以文本方式获取响应体：",response.text)
print(type(response.text))
print("把JSON格式的字符串转换为字典：",response.json())
print(type(response.json()))