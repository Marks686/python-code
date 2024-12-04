#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 陈伟
# @File    : SendMethod.py
# @Project : 12接口测试

import requests


class SendMethod(object):

    @staticmethod
    def send_method(url: str, method: str, params=None, data=None, json=None, headers=None):
        """
        发起get或者post请求的方法
        """
        # 判断是get请求方式
        if method.lower() == 'get':
            # 按照get进行请求
            response = requests.get(url, params=params, headers=headers)
        elif method.lower() == 'post':
            # 判断传参方式是data还是json
            if data is not None:
                response = requests.post(url, data=data, headers=headers)
            elif json is not None:
                response = requests.post(url, json=json, headers=headers)
            else:
                response = requests.post(url, headers=headers)
        elif method.lower() == "delete":
            response = requests.delete(url,headers=headers)
        else:
            print("目前请求方式仅支持get/post/delete")
            return None

        result = {}

        result["status_code"] = response.status_code
        try:
            result["body"] = response.json()
        except Exception as e:
            result["body"] = response.text
        result["headers"] = response.headers
        result['response_time'] = response.elapsed.microseconds / 1000
        return result


if __name__ == '__main__':
    # # 1.准备url
    # url = "http://127.0.0.1:8000/api/get_event_list/"
    # # 2.准备参数
    # payload = {"eid": "1"}

    # 1.准备url
    url = "http://127.0.0.1:8000/api/add_event/"

    # 2.准备参数
    payload = {
        "eid": 10,  # 发布会id
        "name": "苹果发布会3",  # 发布会标题
        "limit": 200,  # 限制人数
        "status": 1,  # 状态
        "address": "成都环球中心",  # 地址
        "start_time": "2023-6-13 10:00:00"  # 发布会时间

    }
    # url = "http://www.httpbin.org/post"

    res = SendMethod.send_method(url, "post", data=payload)
    print(res)
