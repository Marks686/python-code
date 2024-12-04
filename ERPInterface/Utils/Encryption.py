# -*- coding:utf-8 -*-

import hashlib

"""
编写所有的加密方法
"""

def md5_hash(input_string):
    """md5加密的方法"""
    # 创建一个 md5 对象
    m = hashlib.md5()

    # 更新哈希对象的内容
    # 注意：需要将字符串转换为 bytes 类型
    m.update(input_string.encode('utf-8'))

    # 获取十六进制形式的哈希值
    hash_result = m.hexdigest()

    return hash_result



if __name__ == '__main__':
    print(md5_hash("123456Aa"))
