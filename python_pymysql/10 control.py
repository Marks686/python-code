# 1.导包
import pymysql

# 2.创建连接(桥)
conn = pymysql.Connect(
    host="127.0.0.1",
    port=3306,
    database="api_test",
    user="root",
    password="123456",
    charset="utf8",
    autocommit=True     # 自动提交
)

# 3.创建游标(驴)
cur = conn.cursor()

# 4.核心: 执行 sql 语句, 并处理结果 (有差异性)
#查询类操作
sql = "select * from t_area"    # sql语句
cur.execute(sql)    # 执行语句

# 处理结果
# row1 = cur.fetchone()   # 一次拿一行数据, 返回一个元组
# print(row1)
# row2 = cur.fetchone()
# print(row2)

# rows = cur.fetchall()   # 一次性拿所有数据, 返回一个元组, 每行数据也是一个元组
# print(rows)

# 增删改类操作, 以delete为例, 其他都一样
sql = "delete from t_area where area_name = '段智兴'"  # 语句
cur.execute(sql)    # 执行语句
# conn.commit()   # 提交

# 处理结果
print(cur.rowcount)     # 打印受影响的行数

# 5.关闭游标
cur.close()

# 6.关闭连接
conn.close()
