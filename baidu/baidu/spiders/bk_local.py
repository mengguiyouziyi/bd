# -*- coding: utf-8 -*-
import scrapy
import os
import re
from baidu.items import BaikeItem


class BkSpider(scrapy.Spider):
	name = 'bk_local'
	"""
	/data1/spider/menggui/bdbk_html/
	/data/menggui/bdbk_html/
	/home/lijian.sun/bdbk_html/
	"""
	fs = os.listdir(r'/data1/spider/menggui/bdbk_html/')
	start_urls = ['file:///data1/spider/menggui/bdbk_html/%s' % f for f in fs]

	custom_settings = {
		# 'LOG_LEVEL': 'DEBUG',
		'DEFAULT_REQUEST_HEADERS': {},
		'DOWNLOADER_MIDDLEWARES': {},
		'ITEM_PIPELINES': {'baidu.pipelines.MysqlPipeline': 300}
	}

	def parse(self, response):
		print(response.url)
		item = BaikeItem()
		if not response.request.url:
			return
		id = re.search(r'bdbk_html\/(\d+)', response.request.url).group(1)
		quan_cheng = response.xpath('//dd[@lemmaWgt-lemmaTitle-title]//text()').extract_first()
		texts = response.xpath('//div[@class="lemma-summary"]//text()').extract()
		print(texts)
		text = ''.join(texts)
		if not text:
			# print(str(item['id']) + ' no text')
			return

		item['id'] = id
		item['quan_cheng'] = quan_cheng
		item['intro'] = text
		return item
