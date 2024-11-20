# -*- coding:utf-8 -*-

from RabbitMQ import RabbitMQ
import json
from Database import Database
from Redis import RedisManager

mq = RabbitMQ()
db = Database()
redis = RedisManager()

# 回调函数
def call_back(ch,method,properties,body):
    body = json.loads(body.decode())
    # 1.判断good_id是否存在
    sql_good = f"SELECT * from es_goods where id = {body['good_id']}"
    # 2.判断user_id是否存在
    sql_user = f"SELECT * from es_users where id = {body['user_id']}"

    user = db.get_one(sql_user)
    goods = db.get_one(sql_good)
    if user and goods:

        # Redis里面key是否存在，存在就去消费
        result = redis.get_string(body["order_id"])
        if result:

            # es_order表新增一条记录
            sql_order = f"insert into es_order(`good_id`,`good_price`,`good_name`) VALUES({body['good_id']},{body['price']},'{body['good_name']}')"
            # 用户表 es_users 表金额money减少
            sql_money = f"UPDATE es_users set money = money - {body['price']} where id = {body['user_id']}"

            # 商品表 es_goods 表商品的库存（num）减少
            sql_num = f"UPDATE es_goods set num = num - {body['num']} where id = {body['user_id']}"

            try:
                db.execute_sql(sql_num,sql_money,sql_order)
            except Exception as e:
                print(f"执行出现异常：{e}")
            else:
                print("代码执行成功")
                # 消费完毕之后删除Redis里面key
                redis.del_string(body["order_id"])
        else:
            print("redis里面的key不存在，重复消息，不做消费")

    else:
        print("用户或者商品不存在")



    ch.basic_ack(delivery_tag=method.delivery_tag)  # 手动确认消息



# 3.建立通道
channel,connection = mq.connection()

# 4.声明队列
channel.queue_declare(queue="work",durable=True)   # durable=True表示开启了消息队列的持久化
channel.basic_qos(prefetch_count=1)     # 限制每个消费者一次只能处理一条消息

# 5.设置回调函数来消费消息
channel.basic_consume(queue="work",    # 队列名称
                      on_message_callback=call_back    # 回调函数
                      )
# 6.开始消费
channel.start_consuming()

print("消息已经消费完毕")