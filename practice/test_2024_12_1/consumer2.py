
import pika


def call_back(ch,method,properties,body):
    print(body.decode(),flush=True)



# 1. 创建证书，输入账号和密码
credentials = pika.PlainCredentials("admin","123456")

# 2. RabbitMQ连接对象
connection = pika.BlockingConnection(pika.ConnectionParameters(host="192.168.10,151"),credentials=credentials)

# 3. 建立通道
channel = connection.channel()

# 4. 声明交换器
channel.exchange_declare(exchange="log",exchange_type="fanout")

# 5. 声明一个临时队列
result = channel.queue_declare(queue='',exclusive=True)
queue_name = result.method.queue

# 6. 把队列绑定到交换机上面
channel.queue_bind(exchange="log",queue=queue_name)

# 7. 设置回调函数来消费消息
channel.basic_consume(queue=queue_name,
                      on_message_callback=call_back,
                      auto_ack=True)

# 8. 启动消息消费
channel.start_consuming()
print("消息消费启动...")
