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
		'LOG_LEVEL': 'DEBUG',
		'DEFAULT_REQUEST_HEADERS': {},
		'DOWNLOADER_MIDDLEWARES': {},
		'ITEM_PIPELINES': {}
	}

	def parse(self, response):
		item = BaikeItem()
		if not response.request.url:
			return
		id = re.search(r'\d+', response.request.url).group()
		quan_cheng = response.xpath('//dd[@lemmaWgt-lemmaTitle-title]//text()').extract_first()
		texts = response.xpath('//div[@class="lemma-summary"]//text()').extract()
		text = ''.join(texts)
		if not text:
			print(str(item['id']) + ' no text')
			return

		item['id'] = id
		item['quan_cheng'] = quan_cheng
		item['intro'] = text
		return item
