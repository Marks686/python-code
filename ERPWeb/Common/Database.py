# 对pymysql进行 二次封装,方便我们在项目中的使用--面向对象
# 1.封装两个方法,一个方法是获取执行查询之后的一条数据,另外方法是获取所有的数据

import pymysql
from Common.cfg import get_database


class Database(object):
    def __init__(self):
        # 初始化获取数据库的配置
        self.data = get_database()
        # 初始化一个连接对象
        self.db = pymysql.connect(**self.data)

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

    def execute_sql(self, sql):
        """
        修改和删除数据
        :return:
        """
        with self.db.cursor(cursor=pymysql.cursors.DictCursor) as cur:
            try:
                rows = cur.execute(sql)
            except Exception as e:
                print(f"SQL执行失败,原因是:{e}")
            else:
                print(f"影响了{rows}行")
                self.db.commit()




if __name__ == '__main__':
    data = Database()
    sql = 'select * from ecs_users'
    print(data.get_all(sql))