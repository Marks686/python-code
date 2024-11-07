import redis

class RedisManager(object):
    def __init__(self,host,port=6379,max_connections=10,db=0):
        # 创建连接池对象
        self.pool = redis.ConnectionPool(host=host, port=port, max_connections=max_connections, db=db)

        # 使用连接池对象创建客户端
        self.conn = redis.Redis(connection_pool=self.pool)

    """
        redis里面字符串类型的设置
    """
    def set_string(self,key,value):
        self.conn.set(key,value)

    """
        获取redis里面字符串类型的值
    """
    def get_string(self,key):
        return self.conn.get(key)

if __name__ == '__main__':
    redis_test = RedisManager(host="192.168.10.161",db=1)
    redis_test.set_string("age2",100)
    redis_test.get_string("age2")