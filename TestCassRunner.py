# -*- coding:utf-8 -*-  

'''
Created on 2017年3月29日

@author: Jin

'''

import GetToken
import AdminTestCase_01#导入测试用例

hhlist = []
def HRunner():
#     global TestReportData
    print('开始测试')
    GetToken.test_get_token()
    AdminTestCase_01.test_1add_admin()#添加管理员
    AdminTestCase_01.test_2del_admin()#删除管理员
#     print(AdminTestCase_01.hlist)
    TestReportData = AdminTestCase_01.hlist#返回测试结果，不用模块的测试结果在这里用+号连接合并成一个。
#     print(TestReportData)
    print('结束测试')
    hhlist.extend(TestReportData) 


# HRunner()
# print(hhlist)
