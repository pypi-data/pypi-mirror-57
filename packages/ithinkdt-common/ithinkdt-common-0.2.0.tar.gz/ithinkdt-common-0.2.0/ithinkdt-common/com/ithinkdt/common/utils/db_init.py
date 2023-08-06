# -*- coding:utf-8 -*-
"""
    @description: 定义初始化数据库类，在执行UI脚本之前先初始化数据库
    @time: 2019/11/14
    @author: lihui
"""
import os
import subprocess


class DBInit:

    def __init__(self, sql_path, mysql_path, host, port, user, password, database):
        """
        数据库初始化
        :param sql_path: sql文件的存放路径
        :param mysql_path: mysql.exe的本地安装路径
        :param host: host
        :param port: port
        :param user: 用户名
        :param password: 密码
        :param database: 数据库名称
        """
        self.sql_path = sql_path
        self.mysql_path = mysql_path
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    # 使用subprocess 模块产生子进程，并连接到子进程的标准输入、输出、错误中去
    # 创建管道
    @staticmethod
    def subprocess(cmdline, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True):
        p = subprocess.Popen(cmdline, stdout=stdout, stderr=stderr, shell=shell)
        curline = p.stdout.readline()
        while curline != b'':
            print(curline.decode('gbk'))
            curline = p.stdout.readline()

        # 程序结束，获取返回值
        p.wait()
        print(p.returncode)

    def db_init_subprocess(self):
        # 判断配置总读取的sql 文件路径是具体sql 文件还是文件夹
        if os.path.isdir(self.sql_path):
            # 路径是文件夹，循环执行其中的sql 文件
            print('sql 文件路径：' + self.sql_path)
            lst = os.listdir(self.sql_path)
            for c in lst:
                if os.path.splitext(c)[1] == '.sql':
                    cmdline = os.path.join(self.mysql_path, 'bin', 'mysql') + ' -h' + self.host + ' -u' + self.user + ' -p' + self.password \
                              + ' ' + self.database + ' < ' + os.path.join(self.sql_path, c)
                    print('sql 文件：' + c + ' 执行开始----------------')
                    self.subprocess(cmdline)
                    print('sql 文件：' + c + ' 执行结束----------------')
        else:
            print('sql 文件：' + self.sql_path + ' 执行开始----------------')
            cmdline = os.path.join(self.mysql_path, 'bin', 'mysql') + ' -h' + self.host + ' -u' + self.user + ' -p' + self.password \
                      + ' ' + self.database + ' < ' + self.sql_path
            self.subprocess(cmdline)
            print('sql 文件：' + self.sql_path + ' 执行结束----------------')


# if __name__ == '__main__':
#     DBInit(sql_path, mysql_path, host, port, user, password, database).db_init_subprocess()
