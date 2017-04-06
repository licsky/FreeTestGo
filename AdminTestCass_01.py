# -*- coding:utf-8 -*-  

'''
Created on 2017年3月29日

@author: Jin
'''
import json
import requests
import xlrd

Testdata = xlrd.open_workbook('C:/Jin/workpase/ApiTest/src/TestData.xls')#读取测试数据
table = Testdata.sheets()[0]#选择excle表中的sheet
hurl = table.cell(7,1).value#从测试数据中读取url
htoken = table.cell(8,1).value
hcontent_type = table.cell(6,1).value
hlist = []#添加一个数组，用来装测试结果
def test_1add_admin():
    for i in range(3,9):
        table = Testdata.sheets()[1]#选择excle表中的sheet
        username = table.cell(i,0).value#读取测试数据
        realName = table.cell(i,1).value
        status = table.cell(i,2).value
        password = table.cell(i,3).value
        remark = table.cell(i,4).value        
        data = {
                "username": username,
                "realName": realName,
                "password": password,
                "remark": remark,
                "status":status
                }
             
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        r = requests.post(hurl+'/admin/add', data=json.dumps(data), headers=headers)
        hjson = json.loads(r.text)#获取并处理返回的json数据
        hstr = "error"
        if hstr in hjson:
#             print(hjson)
            hhhdata = {"t_id": '1-'+str(i+1), 
                          "t_name": "新增管理接口", 
                          "t_method": "post", 
                          "t_url": hurl+'/admin/add', 
                          "t_param": "username:"+str(username)+",realName:" +str(realName)+",password:"+str(password)+",remark:"+str(remark)+",status:"+str(status),
                          "t_hope": "{code:200,msg:登陆成功}", 
                          "t_actual": str(hjson), 
                          "t_result": "失败"} 
            hlist.append(hhhdata)
            print("添加管理员")
            print('测试不测试通过')
            print("返回的消息为："+str(hjson))
        else:
            hcode = str(hjson['code'])     
            if hcode == table.cell(i,5).value:
                hmsg = str(hjson['msg'])    
                hhhdata = {"t_id": '1-'+str(i+1), 
                          "t_name": "新增管理接口", 
                          "t_method": "post", 
                          "t_url": hurl+'/admin/add', 
                          "t_param": "username:"+str(username)+",realName:" +str(realName)+",password:"+str(password)+",remark:"+str(remark)+",status:"+str(status),
                          "t_hope": "{code:200,msg:新增管理接口}", 
                          "t_actual": 'code:'+str(hcode)+','+'msg:'+str(hmsg), 
                          "t_result": "通过"}    
                hlist.append(hhhdata)#把测试结果添加到数组里面
                print("添加管理员")
                print('测试通过')
                print('请求返回消息为：'+str(hjson['msg']))   
            else:
                hmsg = str(hjson['msg']) 
                hhhdata = {"t_id": '1-'+str(i+1), 
                          "t_name": "新增管理接口", 
                          "t_method": "post", 
                          "t_url": hurl+'/admin/add', 
                          "t_param": "username:"+str(username)+",realName:" +str(realName)+",password:"+str(password)+",remark:"+str(remark)+",status:"+str(status),
                          "t_hope": "{code:200,msg:新增管理接口}", 
                          "t_actual": 'code:'+str(hcode)+','+'msg:'+str(hmsg), 
                          "t_result": "失败"} 
                hlist.append(hhhdata)
                print("添加管理员")
                print('测试不通过')
                print('请求返回状态为：'+hcode)
                print('请求返回消息为：'+str(hjson['msg']))
                print('---------------------------')

def test_2del_admin():
    for i in range(13,16):
        table = Testdata.sheets()[1]#选择excle表中的sheet
        hid = table.cell(i,0).value     
        headers = {
            'content-type': hcontent_type,
            'token': htoken
            }
        r = requests.post(hurl+'/admin/delete?id='+hid, headers=headers)
        hjson = json.loads(r.text)#获取并处理返回的json数据
        hstr = "error"
        if hstr in hjson:
#             print(hjson)
            hhhdata = {"t_id": '2-'+str(i+1), 
                          "t_name": "删除管理员", 
                          "t_method": "post", 
                          "t_url": hurl+'/admin/delete?',
                          "t_param": "id:"+hid,
                          "t_hope": "{code:200,msg:删除成功}", 
                          "t_actual": str(hjson), 
                          "t_result": "失败"} 
            hlist.append(hhhdata)
            print("删除管理员")
            print('测试不通过')
            print("返回的消息为："+str(hjson))
        else:
            hcode = str(hjson['code'])     
            if hcode == table.cell(i,5).value:
                hmsg = str(hjson['msg'])    
                hhhdata = {"t_id": '2-'+str(i+1), 
                          "t_name": "删除管理员", 
                          "t_method": "post", 
                          "t_url": hurl+'/admin/delete?',
                          "t_param": "id:"+hid,
                          "t_hope": "{code:200,msg:删除成功}", 
                          "t_actual": 'code:'+str(hcode)+','+'msg:'+str(hmsg), 
                          "t_result": "通过"}    
                hlist.append(hhhdata)#把测试结果添加到数组里面
                print("删除管理员")
                print('测试通过')
                print('请求返回消息为：'+str(hjson['msg']))   
            else:
                hmsg = str(hjson['msg']) 
                hhhdata = {"t_id": '2-'+str(i+1), 
                          "t_name": "删除管理员", 
                          "t_method": "post", 
                          "t_url": hurl+'/admin/delete?',
                          "t_param": "id:"+hid,
                          "t_hope": "{code:200,msg:新增管理接口}", 
                          "t_actual": 'code:'+str(hcode)+','+'msg:'+str(hmsg), 
                          "t_result": "失败"} 
                hlist.append(hhhdata)
                print("删除管理员")
                print('测试不通过')
                print('请求返回状态为：'+hcode)
                print('请求返回消息为：'+str(hjson['msg']))
                print('---------------------------')


test_1add_admin()
test_2del_admin()
   
                
