# -*- coding: utf-8 -*-
import scrapy
from baidu.utils.get import get_key
from baidu.items import BaikeItem


class BkSpider(scrapy.Spider):
	name = 'bk'
	allowed_domains = ['baidu.com']
	baike_url = 'http://baike.baidu.com/item/{quan_cheng}'

	def start_requests(self):
		while True:
			id_quan_cheng = get_key('id_quan_cheng')

			# 	quan_cheng = 225916
			if not id_quan_cheng:
				continue
			lis = id_quan_cheng.split('~')
			id = int(lis[0])
			quan_cheng = lis[1]
			item = BaikeItem()
			item['id'] = id
			item['quan_cheng'] = quan_cheng
			self.url = self.baike_url.format(quan_cheng=quan_cheng)
			yield scrapy.Request(self.url, meta={'item': item, 'dont_redirect': True}, dont_filter=True)

	def parse(self, response):
		item = response.meta.get('item')
		if not item:
			return
		item['htm'] = response.text
		return item
