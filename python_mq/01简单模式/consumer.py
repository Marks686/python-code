# -*- coding:utf-8 -*-

import pika

# 回调函数
def call_back(ch,method,properties,body):
    print(body.decode(),flush=True)


# 1.创建证书，输入账号和密码
credentials = pika.PlainCredentials("admin", "123456Aa")

# 2.创建RabbitMQ连接对象
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.10.161", credentials=credentials))

# 3.建立通道
channel = connection.channel()

# 4.声明队列
channel.queue_declare(queue="hello")

# 5.设置回调函数来消费消息
channel.basic_consume(queue="hello",    # 队列名称
                      on_message_callback=call_back,     # 回调函数
                      auto_ack=True)        # 是否自动确认消息

# 6.开始消费
channel.start_consuming()

print("消息已经消费完毕")