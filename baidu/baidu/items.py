# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaikeItem(scrapy.Item):
	# define the fields for your item here like:
	id = scrapy.Field()
	quan_cheng = scrapy.Field()
	htm = scrapy.Field()
	intro = scrapy.Field()
	crawl_time = scrapy.Field()