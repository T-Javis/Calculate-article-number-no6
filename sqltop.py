# -*- coding: utf-8 -*-
#!/usr/bin/python

import MySQLdb
import re

from base import BaseModel
def dal():#数据源
	return BaseModel()
dbpost = dal().db


con = MySQLdb.connect(host="10.14.*.*", user="root", passwd="K****V",db="pyspider_resultdb",port=3306)
cur = con.cursor()

#---------------------------------------------
cur.execute('select result,url,taskid,updatetime from zhuanhuayixue_test2')
#---------------------------------------------

db=cur.fetchall()
#print(db)

#(('{"url":" ","ref":" "}',),('{"url":" ","ref":" "}',),(),())


#---------------------------------------------
website='zhuanhuayixue_test2'
#---------------------------------------------


ids_db=dbpost.query('select id from no6_170821')
len_ids=len(ids_db)
id_all=[]
for i in range(0,len_ids):
	id_dic=ids_db[i]
	id_all.append(id_dic['id'])
#print(id_all)
ids=id_all

if max(ids)==None:
	ids=1
else:
	ids=max(ids)+1

#print(len_ids)
#print(ids)

import time
def timestamp_datatime(value):  
    format = '%Y-%m-%d %H:%M'  
    #format = '%Y-%m-%d %H:%M:%S'  
    #value 为时间戳值,如:1460073600.0  
    value = time.localtime(value)  
    dt = time.strftime(format,value)  
    return dt 

def datetime_timestamp(dt):  
    time.strptime(dt,'%Y-%m-%d %H:%M')  
    s = time.mktime(time.strptime(dt,'%Y-%m-%d %H:%M'))  
    return s  

date='2017-06-22 0:0'
limit_time=datetime_timestamp(date)
#print(limit_time)

for i in range(len(db)):
#for i in range(1):	
	#print(i)

	result_db=db[i]
	result_uni=result_db[0]
	url=result_db[1]
	result=result_uni.decode('unicode_escape')
	updatetime=result_db[3]
	#print(result)
	#print('-'*20)
	#print(url)
	#print(updatetime,limit_time)
	if updatetime>limit_time:
		dbpost.execute('insert into no6_170821(article,website,url,id) values (%s,%s,%s,%s)',(result,website,url,ids))
		print(i)
		ids=ids+1






