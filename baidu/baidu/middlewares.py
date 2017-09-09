# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import base64
from random import choice

# 代理服务器
proxyServer = "http://proxy.abuyun.com:9020"

# 1
proxyUser = "H62UV4W5L34VLB1D"
proxyPass = "2BABA9BCA728C5D2"

# 2
# proxyUser = "H20X28E37Z5R11UD"
# proxyPass = "61CE0860F50555CB"

# 3
# proxyUser = "H51N0CWJLZX5981D"
# proxyPass = "24606F3C6193A99D"

# 4
# proxyUser = "HL6O95146U41Z61D"
# proxyPass = "8F2622D2D6A1A73F"

# 5
# proxyUser = "HI4Z5PI5D1Y44S2D"
# proxyPass = "5D698C9C15113ACE"

# for Python 3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta["proxy"] = proxyServer
		request.headers["Proxy-Authorization"] = proxyAuth


class RetryMiddleware(object):
	def process_response(self, request, response, spider):
		if response.status == 429:
			# print('wrong status: %s, retrying~~' % response.status, request.meta['item']['cname'])
			return request.replace(url=request.url)
		else:
			return response

	def process_exception(self, request, exception, spider):
		return request.replace(url=request.url)


class RotateUserAgentMiddleware(object):
	"""Middleware used for rotating user-agent for each request"""

	def __init__(self, agents):
		self.agents = agents

	@classmethod
	def from_crawler(cls, crawler):
		return cls(crawler.settings.get('USER_AGENT_CHOICES', []))

	def process_request(self, request, spider):
		request.headers.setdefault('User-Agent', choice(self.agents))






		# class CustomFaillogMiddleware(object):
		# 	@classmethod
		# 	def from_crawler(cls, crawler):
		# 		return cls()
		#
		# 	def process_response(self, request, response, spider):
		# 		if response.status >= 400:
		# 			reason = response.response_status_message(response.status)
		# 			self._faillog(request, u'HTTPERROR', reason, spider)
		# 		return response
		#
		# 	def process_exception(self, request, exception, spider):
		# 		self._faillog(request, u'EXCEPTION', exception, spider)
		# 		return request
		#
		# 	def _faillog(self, request, errorType, reason, spider):
		# 		with codecs.open('log/faillog.log', 'a', encoding='utf-8') as file:
		# 			file.write("%(now)s [%(error)s] %(url)s reason: %(reason)s \n" %
		# 			           {'now': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
		# 			            'error': errorType,
		# 			            'url': request.url,
		# 			            'reason': reason})
