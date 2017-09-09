# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import codecs
import os


class HtmlWriterPipeline(object):

	def process_item(self, item, spider):
		# path = os.path.abspath('/data1/spider/menggui/cs_bk_html/%s.html' % item['ncid'])
		path = os.path.abspath('/data/menggui/cs_bk_html/%s.html' % item['ncid'])
		# path = os.path.abspath('/home/lijian.sun/cs_bk_html/%s.html' % item['ncid'])
		with codecs.open(path, 'w', 'utf-8') as file:
			file.write(item['htm'])
			print(str(item['ncid']) + ' down success')
		return item


class MysqlPipeline(object):
	"""
	本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
	"""

	def __init__(self):
		self.conn = pymysql.connect(host='etl1.innotree.org', port=3308, user='spider', password='spider', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		# self.conn = pymysql.connect(host='localhost', user='root', password='3646287', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = self.conn.cursor()

	def process_item(self, item, spider):
		# sql = """insert into bdbaike_bj(ncid, cname, intro, crawl_time) VALUES(%s, %s, %s, %s) ON DUPLICATE KEY UPDATE quan_cheng=VALUES(cname), intro=VALUES(intro)"""
		sql = """replace into tyc_jichu_quan_bk_intro (id, quan_cheng, intro, crawl_time) VALUES(%s, %s, %s, %s)"""
		args = (item["id"], item["quan_cheng"], item["intro"], item["crawl_time"])
		self.cursor.execute(sql, args=args)
		self.conn.commit()
		print(str(item['ncid']))

		return item
