# -*- coding: utf-8 -*-
# @Author  : 不温卜火
# @Time    : 2022/1/11 11:55
# @Myblog  : https://buwenbuhuo.blog.csdn.net/

"""
    Name:DataX配置文件批量生成脚本
    作用:批量生成DataX可执行Json文件,可以自动生成某个指定db内与每个表所对应的Json文件
"""
import json
import os

import pymysql

"""
    此部分未封装，感兴趣的可以自行封装下
"""
# 定义MySQL连接属性，根据实际进行修改
mysql_host = "hadoop01"
mysql_port = "3306"
mysql_user = "root"
mysql_passwd = "123456"

#HDFS NameNode相关配置，需根据实际情况作出修改
hdfs_nn_host = "hadoop01"
hdfs_nn_port = "8020"


#获取mysql连接
# 1.连接到mysql数据库
conn = pymysql.connect(host=mysql_host, port=int(mysql_port), user=mysql_user, passwd=mysql_passwd)
# 2.获取游标对象
cursor = conn.cursor()


def get_table_names(db_name: str) -> tuple:
    """
    # 获取表格名称
    :param db_name:自己传参的db名，此处为test
    :return:
    """
    sql_command = "select distinct(table_name) from INFORMATION_SCHEMA.Columns where table_schema='{0}'".format(db_name)
    cursor.execute(sql_command)
    query_data = cursor.fetchall()
    return [item[0] for item in query_data]



def get_column_infors(self, table_name: str, db_name: str) -> tuple:
    """
    获取表格数据类型 针对reader
    :param self:
    :param table_name: XXXXX内的所有表名称
    :param db_name: XXXXX
    :return:
    """
    sql_command = "select column_name, data_type, character_maximum_length, column_comment from INFORMATION_SCHEMA.Columns where table_name='{0}' and table_schema='{1}'".format(
        table_name, db_name)
    self._cursor.execute(sql_command)
    query_data = self._cursor.fetchall()
    return query_data


def get_mysql_meta(database, table):
    """
    获取表格的元数据  包含列名和数据类型 针对reader
    :param database:
    :param table:
    :return:
    """
    sql = "SELECT COLUMN_NAME,DATA_TYPE from information_schema.COLUMNS WHERE TABLE_SCHEMA=%s AND TABLE_NAME=%s ORDER BY ORDINAL_POSITION"
    cursor.execute(sql, [database, table])
    fetchall = cursor.fetchall()
    # cursor.close()
    return fetchall


def get_mysql_columns(database, table):
    """
    获取mysql表的列名
    :param database:
    :param table:
    :return:
    """
    return list(map(lambda x: x[0], get_mysql_meta(database, table)))


def get_hive_columns(database, table):
    """
    将获取的元数据中mysql的数据类型转换为hive的数据类型  写入到hdfswriter中
    :param database: db
    :param table: 表格
    :return:
    """
    def type_mapping(mysql_type):
        mappings = {
            "bigint": "bigint",
            "int": "bigint",
            "smallint": "bigint",
            "tinyint": "bigint",
            "decimal": "string",
            "double": "double",
            "float": "float",
            "binary": "string",
            "char": "string",
            "varchar": "string",
            "datetime": "string",
            "time": "string",
            "timestamp": "string",
            "date": "string",
            "text": "string"
        }
        return mappings[mysql_type]

    meta = get_mysql_meta(database, table)
    return list(map(lambda x: {"name": x[0], "type": type_mapping(x[1].lower())}, meta))


def generate_json(source_database, source_table):
    """
    生成json文件
    :param source_database: test
    :param source_table:
    :return:
    """
    job = {
        "job": {
            "setting": {
                "speed": {
                    "channel": 3
                },
                "errorLimit": {
                    "record": 0,
                    "percentage": 0.02
                }
            },
            "content": [{
                "reader": {
                    "name": "mysqlreader",
                    "parameter": {
                        "username": mysql_user,
                        "password": mysql_passwd,
                        "column": get_mysql_columns(source_database, source_table),
                        "splitPk": "",
                        "connection": [{
                            "table": [source_table],
                            "jdbcUrl": ["jdbc:mysql://" + mysql_host + ":" + mysql_port + "/" + source_database]
                        }]
                    }
                },
                "writer": {
                    "name": "hdfswriter",
                    "parameter": {
                        "defaultFS": "hdfs://" + hdfs_nn_host + ":" + hdfs_nn_port,
                        "fileType": "text",
                        "path": "${targetdir}",
                        "fileName": source_table,
                        "column": get_hive_columns(source_database, source_table),
                        "writeMode": "append",
                        "fieldDelimiter": "\t",
                        "compress": "gzip"
                    }
                }
            }]
        }
    }
    with open(os.path.join("D:\\test", ".".join([source_database, source_table, "json"])), "w") as f:
        json.dump(job, f, sort_keys=True, indent=4, separators=(',', ':'), ensure_ascii=False)


def main(source_database):
    """
    遍历表格内容
    :param source_database:
    :param source_table:
    :return:
    """
    source_database = source_database
    for x in get_table_names("test"):
        generate_json(source_database, x)

if __name__ == '__main__':
    main('test')