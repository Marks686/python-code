# -*- coding:utf-8 -*-
from flask import Flask,request,jsonify
import uuid
from Redis import RedisManager
from RabbitMQ import RabbitMQ
import json

redis = RedisManager()
mq = RabbitMQ()

app = Flask(__name__)

@app.route("/api",methods=["POST"])
def test_api():
    if request.is_json:
        data = request.get_json()
        print(data)
        name = data.get("name","")
        if name:
            return jsonify({"code":200,"message":"请求成功"})
        else:
            return jsonify({"code": 400, "message": "参数错误"})
    else:
        return jsonify({"code": 500, "message": "参数格式错误"})


@app.route("/api/order/add",methods=["POST"])
def add_order():
    if request.is_json:
        # 1.获取接口传递的参数
        data = request.get_json()

        num = data.get("num","")
        good_id = data.get("good_id","")
        good_name = data.get("good_name","")
        price = data.get("price","")
        user_id = data.get("user_id","")

        if num and good_id and good_name and price and user_id:
            # 2.生成一个为一个标识，加入到参数里面
            order_id = str(uuid.uuid4())

            message = {"num": num, "good_id": good_id, "good_name": good_name,
                       "price": price, "user_id": user_id}
            try:
                # 3.构造一个Redis的key,往Redis里面存一份数据，key为唯一标识
                redis.set_string(order_id,str(message))

                # 4.构造一个RabbitMQ的消息,往RabbitMQ里面传递一条消息，包含唯一标识
                message["order_id"] = order_id
                mq.send_message(json.dumps(message))

            except Exception as e:
                print(f"存数据或者发消息的时候出现异常：{e}")
                return jsonify({"code": 300, "message": "程序异常"}), 300
            else:
                return jsonify({"code": 200, "message": "请求成功"}), 200
        else:
            return jsonify({"code": 400, "message": "缺少参数"}),400
    else:
        return jsonify({"code": 500, "message": "参数格式错误"}),500


if __name__ == '__main__':
    app.run(debug=True)