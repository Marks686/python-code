# -*- coding:utf-8 -*-
import redis


class RedisManager(object):
    def __init__(self,host="192.168.10.161",port=6379,max_connections=10,db=0):
        # 创建连接池对象
        self.pool = redis.ConnectionPool(host=host, port=port, max_connections=max_connections, db=db)

        # 使用连接池对象来创建redis客户端
        self.conn = redis.Redis(connection_pool=self.pool)

    def set_string(self,key,value):
        """
        redis里面字符串类型的设置
        :param key: 键
        :param value: 值
        """
        # 有可能存在一些业务上的代码
        self.conn.set(key, value)

    def get_string(self,key):
        """
        获取redis里面字符串的值
        :param key: 需要获取值的键
        :return:
        """
        return self.conn.get(key)

    def del_string(self,key):
        """
        删除键
        :param key:
        :return:
        """
        self.conn.delete(key)

if __name__ == '__main__':
    redis_test = RedisManager(host="192.168.10.161",db=1)
    redis_test.set_string("age2",100)
    print(redis_test.get_string("age2"))








