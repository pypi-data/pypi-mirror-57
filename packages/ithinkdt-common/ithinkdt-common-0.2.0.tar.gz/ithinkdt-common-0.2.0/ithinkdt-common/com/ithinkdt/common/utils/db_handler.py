# -*-coding:utf-8-*-
"""
数据库操作父类，主要用于连接数据库，并执行sql语句操作
"""

import pymysql


class DBHandler:
    """定义DBHandler父类，在middleware中的子类MyDBHandler继承，子类初始化连接数据库，读取配置文件中的数据库信息。
    这样父类可以作为公共的数据库连接类"""
    def __init__(self,
                 host=None,
                 port=3306,
                 user='root',
                 password='',
                 charset='utf8',
                 database=None,
                 **kwargs):

        self.conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            charset=charset,
            database=database,
            **kwargs
        )

        self.cursor = self.conn.cursor()

    """查询功能，返回一条记录"""
    def query_one(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        data = self.cursor.fetchone()
        return data

    """查询功能，返回所有记录"""
    def query_all(self, sql, args=None):
        self.cursor.execute(sql, args)
        self.conn.commit()
        data = self.cursor.fetchall()
        return data

    """查询功能，根据条件选择返回一条还是多条记录"""
    def query(self, sql, args, one=True):
        if one:
            return self.query_one(sql, args)
        else:
            return self.query_all(sql, args)

    """数据库更新操作，慎用，不得已才使用直接更改数据库的方式，一般用接口进行操作"""
    def update(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    """关闭游标，关闭数据库连接"""
    def close(self):
        self.cursor.close()
        self.conn.close()

