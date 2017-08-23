# -*- coding: utf-8 -*-
#!/usr/bin/python

import os
import logging
import sys
import re
from base import BaseModel


prog_path = os.path.abspath(os.path.dirname(__file__))


logging.basicConfig(level=logging.INFO,   #--设置日志等级 CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
		format='%(asctime)s %(filename)s:%(lineno)d %(levelname)s %(message)s',
		filename=os.path.join(prog_path, 'count3.log'),
		filemode='w')
logger = logging.getLogger('mylogger')

def dal():
	return BaseModel()
db = dal().db


data_db=db.query('select id,title,doi from pubmed170731_no6')
data2_db=db.query('select id,article,website from no6_170821')
db.execute('update pubmed170731_no6 set cexuzhongguo=0,shengwugu=0,zhuanhuayixue=0,shengwutansuo=0,dingxiangtong=0,shengwutong=0,lvgushengwu=0,shengwu360=0,jiyincexuchanye=0,yimaitong=0,kexuewang=0,xinshengwu=0,jiyinshidai=0')
#print(data_db)
#print(data2_db)

for i in range(0,len(data_db)):
	n=0
	m=0
	data_list=data_db[i]
	ids=data_list['id']
	title=data_list['title']
	doi=data_list['doi']	
	if doi==None:  #do not have doi
		doi_new='abcdefghuxyz'
	else:
		doi_new=doi[:-1]
	#print(doi_new)

	if title[-20:] == '...  - PubMed - NCBI':
		title=title[:-20]
	if title[-18:] == '.  - PubMed - NCBI':
		title=title[:-18]
	if title[-18:]=='?  - PubMed - NCBI':
		title=title[:-18]



	s1=' -- '
	s2='--'
	s3=' — '
	if s1 in title:
		title=title.replace(' -- ',' ')
		#print('t3'+title)
	if s2 in title:
		title=title.replace('--',' ')
		#print('t3'+title)
	if s3 in title:
		title=title.replace(' — ',' ')

	title2=title.lower()



	#print(i)
	#print(ids)
	#print(title)
	#print(doi_new)
	#print('-'*20)

	

	for x in range(0,len(data2_db)):
		print(i,x)
		data2_list=data2_db[x]
		ids2=data2_list['id']
		article=data2_list['article']
		article2=article.replace('\r\n',' ') #remove the \r\n
		if s1 in article2:
			article2=article2.replace(' -- ',' ')
		if s2 in article2:
			article2=article2.replace('--',' ')
		if s3 in article2:
			article2=article2.replace(' — ',' ')
		article3=article2.lower()
		website=data2_list['website']
		#print(ids2,website)
		if (len(title2)>=40) and (len(doi_new)>4):		#limition of title and doi	
			if (title2 in article3) or (doi_new in article3):
				#print(ids)
				#print(title2,doi_new)
				#print('-'*20)
				#print(article3)
				logger.info('n,ids,ids2:%s,%s,%s'% (n,ids,ids2))
				n=n+1
				if website=='cexu3':
					w_data=db.query('select cexuzhongguo from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['cexuzhongguo']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set cexuzhongguo=%s where id=%s',(website_data_update,ids))
					#logger.info(website)
					#logger.info(website_data)
				elif website=='shengwugu4':
					w_data=db.query('select shengwugu from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwugu']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwugu=%s where id=%s',(website_data_update,ids))
				elif website=='zhuanhuayixue_test2':
					w_data=db.query('select zhuanhuayixue from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['zhuanhuayixue']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set zhuanhuayixue=%s where id=%s',(website_data_update,ids))
				elif website=='shengwutansuo_test2':
					w_data=db.query('select shengwutansuo from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwutansuo']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwutansuo=%s where id=%s',(website_data_update,ids))
				elif website=='dingxiangtong':
					w_data=db.query('select dingxiangtong from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['dingxiangtong']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set dingxiangtong=%s where id=%s',(website_data_update,ids))
				elif website=='shengwutong':
					w_data=db.query('select shengwutong from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwutong']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwutong=%s where id=%s',(website_data_update,ids))
				elif website=='lvgushengwu':
					w_data=db.query('select lvgushengwu from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['lvgushengwu']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set lvgushengwu=%s where id=%s',(website_data_update,ids))
				elif website=='shengwu360_test':
					w_data=db.query('select shengwu360 from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwu360']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwu360=%s where id=%s',(website_data_update,ids))
				elif website=='jiyincexuchanye':
					w_data=db.query('select jiyincexuchanye from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['jiyincexuchanye']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set jiyincexuchanye=%s where id=%s',(website_data_update,ids))
				elif website=='yimaitong_test1':
					w_data=db.query('select yimaitong from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['yimaitong']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set yimaitong=%s where id=%s',(website_data_update,ids))
				elif website=='kexuewang2':
					w_data=db.query('select kexuewang from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['kexuewang']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set kexuewang=%s where id=%s',(website_data_update,ids))
				elif website=='xinshengwu1':
					w_data=db.query('select xinshengwu from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['xinshengwu']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set xinshengwu=%s where id=%s',(website_data_update,ids))
				elif website=='jiyinshidai':
					w_data=db.query('select jiyinshidai from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['jiyinshidai']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set jiyinshidai=%s where id=%s',(website_data_update,ids))


		elif (len(title2)>=50) and (len(doi_new)<=4):
			if (title2 in article3):
				logger.info('m,ids,ids2:%s,%s,%s'% (m,ids,ids2))
				m=m+1
				if website=='cexu3':
					w_data=db.query('select cexuzhongguo from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['cexuzhongguo']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set cexuzhongguo=%s where id=%s',(website_data_update,ids))
					#logger.info(website)
					#logger.info(website_data)
				elif website=='shengwugu4':
					w_data=db.query('select shengwugu from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwugu']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwugu=%s where id=%s',(website_data_update,ids))
				elif website=='zhuanhuayixue_test2':
					w_data=db.query('select zhuanhuayixue from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['zhuanhuayixue']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set zhuanhuayixue=%s where id=%s',(website_data_update,ids))
				elif website=='shengwutansuo_test2':
					w_data=db.query('select shengwutansuo from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwutansuo']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwutansuo=%s where id=%s',(website_data_update,ids))
				elif website=='dingxiangtong':
					w_data=db.query('select dingxiangtong from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['dingxiangtong']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set dingxiangtong=%s where id=%s',(website_data_update,ids))
				elif website=='shengwutong':
					w_data=db.query('select shengwutong from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwutong']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwutong=%s where id=%s',(website_data_update,ids))
				elif website=='lvgushengwu':
					w_data=db.query('select lvgushengwu from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['lvgushengwu']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set lvgushengwu=%s where id=%s',(website_data_update,ids))
				elif website=='shengwu360_test':
					w_data=db.query('select shengwu360 from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['shengwu360']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set shengwu360=%s where id=%s',(website_data_update,ids))
				elif website=='jiyincexuchanye':
					w_data=db.query('select jiyincexuchanye from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['jiyincexuchanye']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set jiyincexuchanye=%s where id=%s',(website_data_update,ids))
				elif website=='yimaitong_test1':
					w_data=db.query('select yimaitong from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['yimaitong']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set yimaitong=%s where id=%s',(website_data_update,ids))
				elif website=='kexuewang2':
					w_data=db.query('select kexuewang from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['kexuewang']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set kexuewang=%s where id=%s',(website_data_update,ids))
				elif website=='xinshengwu1':
					w_data=db.query('select xinshengwu from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['xinshengwu']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set xinshengwu=%s where id=%s',(website_data_update,ids))
				elif website=='jiyinshidai':
					w_data=db.query('select jiyinshidai from pubmed170731_no6 where id=%s',(ids,))
					w_data_list=w_data[0]
					website_data=w_data_list['jiyinshidai']
					website_data_update=website_data+1
					db.execute('update pubmed170731_no6 set jiyinshidai=%s where id=%s',(website_data_update,ids))



					
#-------------------------total_no6------------------------------------
cexuzhongguo_weight=1
shengwugu_weight=1
zhuanhuayixue_weight=1
shengwutansuo_weight=1
dingxiangtong_weight=1
shengwutong_weight=1
lvgushengwu_weight=1
shengwu360_weight=1
jiyincexuchanye_weight=2
yimaitong_weight=0.5
kexuewang_weight=2
xinshengwu_weight=1
jiyinshidai_weight=1


db.execute('update pubmed170731_no6 set total=0')
data_db=db.query('select * from pubmed170731_no6')
for i in range(0,len(data_db)):
	data_list=data_db[i]
	ids=data_list['id']
	total=data_list['total']
	cexuzhongguo=data_list['cexuzhongguo']
	shengwugu=data_list['shengwugu']
	zhuanhuayixue=data_list['zhuanhuayixue']
	shengwutansuo=data_list['shengwutansuo']
	dingxiangtong=data_list['dingxiangtong']
	shengwutong=data_list['shengwutong']
	lvgushengwu=data_list['lvgushengwu']
	shengwu360=data_list['shengwu360']
	jiyincexuchanye=data_list['jiyincexuchanye']
	yimaitong=data_list['yimaitong']
	kexuewang=data_list['kexuewang']
	xinshengwu=data_list['xinshengwu']
	jiyinshidai=data_list['jiyinshidai']
	#total=cexuzhongguo+shengwugu+zhuanhuayixue+shengwutansuo+dingxiangtong+shengwutong+lvgushengwu+shengwu360+jiyincexuchanye+yimaitong+kexuewang+xinshengwu+jiyinshidai
	total=cexuzhongguo_weight*cexuzhongguo+shengwugu_weight*shengwugu+zhuanhuayixue_weight*zhuanhuayixue+shengwutansuo_weight*shengwutansuo+dingxiangtong_weight*dingxiangtong+shengwutong_weight*shengwutong+lvgushengwu_weight*lvgushengwu+shengwu360_weight*shengwu360+jiyincexuchanye_weight*jiyincexuchanye+yimaitong_weight*yimaitong+kexuewang_weight*kexuewang+xinshengwu_weight*xinshengwu+jiyinshidai_weight*jiyinshidai
	db.execute('update pubmed170731_no6 set total=%s where id=%s',(total,ids))
	print(i,total)
	logger.info(i)
	logger.info(total)
	








		