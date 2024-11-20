# -*- coding:utf-8 -*-

import pika

# 1.创建证书，输入账号和密码
credentials = pika.PlainCredentials("admin", "123456Aa")

# 2.创建RabbitMQ连接对象
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.10.161", credentials=credentials))

# 3.建立通道
channel = connection.channel()

# 4.声明队列
channel.queue_declare(queue="work",durable=True)    # durable=True表示开启了消息队列的持久化

# 5.发送消息到队列
message = "hello world6"
channel.basic_publish(
    exchange='',            # 交换机
    routing_key="work",    # 路由，需要和队列名称对应上
    body= message,    # 消息体，也就是要发送什么数据
    properties=pika.BasicProperties(delivery_mode=2)    # 消息持久化
)


print(f"消息已经发送成功了：{message}")

# 6.关闭连接
connection.close()
