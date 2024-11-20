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

# 4.声明直接交换器
channel.exchange_declare(exchange="direct_logs", exchange_type="direct")

# 5.声明一个临时队列
result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue

# 6.把队列绑定到交换器上面
channel.queue_bind(exchange='direct_logs',
                   queue=queue_name,
                   routing_key="error")


# 7.设置回调函数来消费消息
channel.basic_consume(queue=queue_name,    # 队列名称
                      on_message_callback=call_back,     # 回调函数
                      auto_ack=True)        # 是否自动确认消息

# 8.开始消费
channel.start_consuming()

print("消息已经消费完毕")