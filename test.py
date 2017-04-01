# -*- coding:utf-8 -*-  

'''
Created on 2017年3月30日

@author: Jin
'''
import re     
f = open("C:\\Users\\admin\\Desktop\\daima.txt","r") #打开这个XX路径下的XX.txt文件并读取
zhPattern = re.compile(u'[\u4e00-\u9fa5]+') #调取判断中文的函数
for (num,line) in enumerate(f):                 #读取当前文档的每一行的行号和内容
    match = zhPattern.search(line)              #把读取的值传到函数里进行判断有没有中文
    if match:                                   #如果有。。。
        print ("第",num,"行有中文:",line)
    else:
        pass
     

