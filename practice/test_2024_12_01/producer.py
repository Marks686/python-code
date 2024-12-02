

import pika
# 1. 创建证书，输入账号密码
credentials = pika.PlainCredentials('admin', '123456')

# 2. 创建RabbitMQ连接对象
con = pika.ConnectionParameters(host='192.168.1.151', credentials=credentials)
connection = pika.BlockingConnection(con)

# 3. 建立通道
channel = connection.channel()

# 4. 声明扇形交换器
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 5. 发送消息到队列
message = 'Hello World!'
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

print(f"消息已经发送成功了：{message}")

# 6.关闭连接
connection.close()