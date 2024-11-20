# -*- coding:utf-8 -*-

import pika

# 1.创建证书，输入账号和密码
credentials = pika.PlainCredentials("admin", "123456Aa")

# 2.创建RabbitMQ连接对象
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.10.161", credentials=credentials))

# 3.建立通道
channel = connection.channel()

# 4.声明直接交换器
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

# 5.发送消息到队列
message = "hello world error"
routing_key = "error"    # 设置路由键
channel.basic_publish(
    exchange='direct_logs',  # 交换机
    routing_key=routing_key,
    body=message  # 消息体，也就是要发送什么数据
)

print(f"消息已经发送成功了：{message}")

# 6.关闭连接
connection.close()
