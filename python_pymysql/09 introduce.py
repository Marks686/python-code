# pymysql 不论是哪种操作, 流程基本都一致
# 1.导包
# 2.创建连接(桥)
# 3.创建游标(驴)
# 4.核心: 执行 sql 语句, 并处理结果 (有差异性)
# 5.关闭游标
# 6.关闭连接

# 1.导包
import pymysql

# 2.创建连接(桥)
conn = pymysql.Connect(
    host="127.0.0.1",
    port=3306,
    database="api_test",
    user="root",
    password="123456",
    charset="utf8"
)
print(conn)
# 3.创建游标(驴)
cur = conn.cursor()
print(cur)
# 4.核心: 执行 sql 语句, 并处理结果 (有差异性)
sql = "select * from t_area"
cur.execute(sql)
print(cur.fetchone())

# 5.关闭游标
cur.close()

# 6.关闭连接
conn.close()
