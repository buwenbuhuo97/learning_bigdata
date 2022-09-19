# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/1/10 21:18
# @Myblog  : https://buwenbuhuo.blog.csdn.net/
# pip install -i https://pypi.douban.com/simple/ matplotlib

from datetime import datetime
import pymysql

TITLE_HEAD = """# {system_name}数据库设计文档
文档版本:1.0.0.0
发布时间：{now}
文档描述：
本文档是{system_name}数据库设计文档，数据库是 `Mysql`，以下将主要说明：`字段名称`、`字段类型`、`字段长度`、以及`字段解释`。
作者：不温卜火
MyBlog:https://buwenbuhuo.blog.csdn.net/


"""
# 输出样式
TABLE_HEADER = """## {num}. {table_name}

| 序号 | 字段名称    | 数据类型 | 长度 | 解释说明   |
| :--: | :---------: | :------: | :--: | :--------: |"""


TABLE_BODY = """
| {index}    | {field} | {field_type}  | {field_leght}   | {field_explain} |"""


TABLE_TAIL = """
\n
\n
"""


class ExportDatabaseField():
    def __init__(self, system_name: str, database_params: dict):
        """
        初始化配置
        :param system_name:
        :param database_params:
        """
        self._system_name = system_name
        self._params = database_params
        self._database_connect = None
        self._cursor = None
        self._connect_database_server()

    def _connect_database_server(self) -> None:
        """
        连接db服务
        :return:
        """
        self._database_connect = pymysql.connect(**self._params)
        self._cursor = self._database_connect.cursor()

    def close_connect(self) -> None:
        """
        关闭连接
        :return:
        """
        self._cursor.close()
        self._database_connect.close()
        self._cursor = None
        self._database_connect = None

    def _verify_connection(self) -> None:
        """
        测试连接是否成功
        :return:
        """
        ret = False
        try:
            self._database_connect.ping()
            ret = True
        except Exception as err:
            self.close_connect()
            self._connect_database_server()
        return ret

    def get_table_names(self, db_name: str) -> tuple:
        """
        得到数据库中表的名称
        :param db_name:
        :return:
        """
        sql_command = "select distinct(table_name) from INFORMATION_SCHEMA.Columns where table_schema='{0}'".format(db_name)
        self._cursor.execute(sql_command)
        query_data = self._cursor.fetchall()
        return [item[0] for item in query_data]

    def get_column_infors(self, table_name: str, db_name: str) -> tuple:
        """
        得到数据库中表的详细信息
        :param table_name: 表的名称
        :param db_name: 库的名称
        :return:
        """
        sql_command = "select column_name, data_type, character_maximum_length, column_comment from INFORMATION_SCHEMA.Columns where table_name='{0}' and table_schema='{1}'".format(table_name, db_name)
        self._cursor.execute(sql_command)
        query_data = self._cursor.fetchall()
        return query_data

    def save_into_file(self, file_name: str) -> object:
        """
        保存成md文件
        :param file_name:
        :return:
        """
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        system_name = self._system_name
        file_name = "{0}.md".format(file_name)
        database_name = self._params["database"]

        with open(file_name, "w", encoding="utf8") as file_obj:
            file_obj.write(TITLE_HEAD.format(system_name=system_name, now=now))

            table_names = self.get_table_names(database_name)
            for num, table in enumerate(table_names, start=1):
                table_infos = self.get_column_infors(table, database_name)
                file_obj.write(TABLE_HEADER.format(num=num, table_name=table))

                for index, info in enumerate(table_infos, start=1):
                    content = TABLE_BODY.format(index=index, field=info[0], field_type=info[1], field_leght=info[2] if info[2] else "", field_explain=info[3])
                    file_obj.write(content)

                file_obj.write(TABLE_TAIL)


def main():
    """
    数据库连接配置
    :return:
    """
    database_confis = {"database": "social",
                       "host": "127.0.0.1",
                       "port": 3306,
                       "user": "root",
                       "password": "123456",
                       "charset": "utf8"}

    system_name = ""

    factory = ExportDatabaseField
    instance = factory(system_name, database_confis)

    file_name = "{0}数据库设计文档".format(system_name)
    instance.save_into_file(file_name)


# 主程序启动入口
if __name__ == "__main__":
    main()