import pymysql


class Database(object):
    def __init__(self,host="192.168.10.161",port=3306,
                 user="root",password="Beimengkj123@",
                 database='ecshop',charset="utf8"):
        # 初始化一个连接对象
        self.db = pymysql.connect(host=host,port=port,user=user,password=password,
                                  database=database,charset=charset)

    def get_one(self, sql):
        """
        查询之后获取一条数据
        :param sql:
        :return:
        """
        # 使用cfg来获取配置文件的数据,然后拆包的方式传入数据
        with self.db.cursor(cursor=pymysql.cursors.DictCursor) as cur:
            cur.execute(sql)
            return cur.fetchone()

    def get_all(self, sql):
        """
        查询之后获取多条数据
        :param sql:
        :return:
        """
        with self.db.cursor(cursor=pymysql.cursors.DictCursor) as cur:
            cur.execute(sql)
            return cur.fetchall()

    def execute_sql(self, *sqls):
        """
        修改和删除数据
        :return:
        """
        with self.db.cursor(cursor=pymysql.cursors.DictCursor) as cur:
            self.db.begin()
            try:
                for sql in sqls:
                    rows = cur.execute(sql)
            except Exception as e:
                print(f"SQL执行失败,原因是:{e}")
                self.db.rollback()
            else:
                print(f"影响了{rows}行")
                self.db.commit()




if __name__ == '__main__':
    data = Database()
    sql = 'select * from es_users'
    print(data.get_all(sql))