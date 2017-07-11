# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from random import choice

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 代理隧道验证信息
# proxyUser = "H4XGPM790E93518D"
# proxyPass = "2835A47D56143D62"


# proxyUser = "HS42FV2R583524HD"
# proxyPass = "BB5F3DAE917E484E"

# proxyUser = "H20X28E37Z5R11UD"
# proxyPass = "61CE0860F50555CB"

proxyUser = "H51N0CWJLZX5981D"
proxyPass = "24606F3C6193A99D"

# proxyUser = "HL6O95146U41Z61D"
# proxyPass = "8F2622D2D6A1A73F"
#

# proxyUser = "HQ78N3Y82239165D"
# proxyPass = "AA99073C3271DBFA"
#

# proxyUser = "HI4Z5PI5D1Y44S2D"
# proxyPass = "5D698C9C15113ACE"

# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta["proxy"] = proxyServer
		request.headers["Proxy-Authorization"] = proxyAuth


class RetryMiddleware(object):
	def process_response(self, request, response, spider):
		if response.status == 429:
			# print('wrong status: %s, retrying~~' % response.status, request.meta['item']['quan_cheng'])
			return request.replace(url=request.url)
		else:
			return response


class RotateUserAgentMiddleware(object):
	"""Middleware used for rotating user-agent for each request"""

	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.get('USER_AGENT_CHOICES', []))

	def process_request(self, request, spider):
		request.headers.setdefault('User-Agent', choice(self.agents))


