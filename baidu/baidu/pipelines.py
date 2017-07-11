# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# import pymysql
import codecs
import os


class HtmlWriterPipeline(object):
	def process_item(self, item, spider):
		path = os.path.abspath('/data/menggui/bdbk_html/%s.html' % item['id'])

		with codecs.open(path, 'wb') as file:
			file.write(item['htm'])
		return item


	# class MysqlPipeline(object):
	# 	"""
	# 	本机 localhost；公司 etl2.innotree.org；服务器 etl1.innotree.org
	# 	"""
	#
	# 	def __init__(self):
	# 		self.conn = pymysql.connect(host='etl1.innotree.org', user='spider', password='spider', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	# 		# self.conn = pymysql.connect(host='localhost', user='root', password='3646287', db='spider', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
	# 		self.cursor = self.conn.cursor()
	#
	# 	def process_item(self, item, spider):
	# 		sql = """insert into bdbaike_bj(id, quan_cheng, htm) VALUES(%s, %s, %s) ON DUPLICATE KEY UPDATE quan_cheng=VALUES(quan_cheng),  htm=VALUES(htm)"""
	# 		args = (item["id"], item["quan_cheng"], item["htm"])
	# 		self.cursor.execute(sql, args=args)
	# 		self.conn.commit()
	# 		# print(str(item['com_id']) + ' success')
	# 		print(str(item['id']) + ' success')
