# -*- coding:utf-8 -*-  

'''
Created on 2017年3月31日

@author: Jin
'''
import threading    #导入多线程库
import TestCassRunner


def hthreads():
    threads = []    #创建线程数组
    h1 = threading.Thread(target=TestCassRunner.HRunner)   #定义线程
    threads.append(h1)      #添加线程到数组
#     h2 = threading.Thread(target=TestCassRunner.HRunner)   #定义线程
#     threads.append(h2)      #添加线程到数组
    
    for h in threads:   #读取数组里的所有线程，并同时执行
        h.setDaemon(True)   #将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
        h.start()       #开始线程活动
            
    h.join()    #把主线程挂起，等待上面的线程跑完了再运行
    
    AllTestReportData = TestCassRunner.hhlist
        
#     print(AllTestReportData)
   
    return AllTestReportData

# hthreads()
