#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 陈伟
# @File    : GetKeywords.py
# @Project : InterfaceTest


import jsonpath


class GetKeywords(object):

    @staticmethod
    def get_keyword(data, name):
        try:
            result = jsonpath.jsonpath(data, f'$..{name}')[0]
        except Exception as e:
            print(f"{name} 数据没有取到")
            return False
        return result

    @staticmethod
    def get_keywords(data, name):
        try:
            result = jsonpath.jsonpath(data, f'$..{name}')
        except Exception as e:
            print(f"{name} 数据没有取到")
            return False
        return result


if __name__ == '__main__':
    data = {
        "status_code": 200,
        "body": {
            "code": 200,
            "message": "获取验证码成功",
            "data": "404565",
            "list": [
                {"name": "jack"},
                {"name": "king", "like": [
                    "唱跳",
                    "rap",
                    "篮球"
                ]}
            ]
        },
        "headers": {
            "Vary": "Origin, Access-Control-Request-Method, Access-Control-Request-Headers",
            "X-Content-Type-Options": "nosniff",
            "X-XSS-Protection": "1; mode=block",
            "Cache-Control": "no-cache, no-store, max-age=0, must-revalidate",
            "Pragma": "no-cache",
            "Expires": "0",
            "X-Frame-Options": "DENY",
            "Content-Type": "application/json",
            "Transfer-Encoding": "chunked",
            "Date": "Mon, 19 Jun 2023 03:21:01 GMT",
            "Keep-Alive": "timeout=60",
            "Connection": "keep-alive"
        },
        "response_time": 20.684
    }

    # print(data["body"]['list'][1]["name"])
    #
    # # jsonpath.jsonpath("json对象","提取规则")
    # print(jsonpath.jsonpath(data, "$..name"))

    print(GetKeywords.get_keywords(data, "name"))
