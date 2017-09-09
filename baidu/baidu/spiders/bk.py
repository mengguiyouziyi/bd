# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from baidu.utils.get import get_key
from baidu.items import BaikeItem
from baidu.settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT


class BkSpider(scrapy.Spider):
	name = 'bk'
	allowed_domains = ['baidu.com']
	baike_url = 'http://baike.baidu.com/item/{cname}'

	def start_requests(self):
		while True:
			ncid_cname = get_key('baike_ncid_cname')
			# 	ncid_cname = 225916
			if not ncid_cname:
				continue
			lis = ncid_cname.split('~')
			id = int(lis[0])
			quan_cheng = lis[1]
			item = BaikeItem()
			item['id'] = id
			item['quan_cheng'] = quan_cheng
			self.url = self.baike_url.format(cname=quan_cheng)
			yield scrapy.Request(self.url, meta={'item': item}, dont_filter=True)

	def parse(self, response):
		item = response.meta.get('item')
		if not item:
			return
		text = response.text
		if not text:
			# print(str(item['ncid']) + ' no text')
			return
		intro = response.xpath('//div[@class="lemma-summary"]//text()').extract()
		if not intro:
			return
		intro = ''.join([x.strip() for x in intro])
		# item['htm'] = response.text
		item['intro'] = intro
		item["crawl_time"] = datetime.now().strftime(SQL_DATETIME_FORMAT)

		return item
