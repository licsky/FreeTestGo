# -*- coding:utf-8 -*-  
'''
Created on 2017年4月3日

@author: Jin
'''
import pymysql

def ConnectData(host,sql):
    connect = pymysql.Connect(
        host=host,
        port=8066,
        user='mala',
        passwd='Mala123456$',
        db='boss',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()
    # 查询数据
    sql = sql    
    cursor.execute(sql ) #执行sql
    print('共查找出', cursor.rowcount, '条数据')    
    if cursor.rowcount ==0:
        print("数据库中没有找到你要的值")
        return 0
    else:
        for hrow in cursor.fetchall():      
#             print(hrow)
            return hrow

    cursor.close()
    connect.close()
#     return hrow
host='192.168.0.1'
sql = "SELECT id,user_name FROM t_admin  where user_name like 'jinte111st'"
print(ConnectData(host,sql))
# print("返回值是："+ConnectData(host,sql)[1])


#
