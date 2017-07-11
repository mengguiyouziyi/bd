from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy import log
import os, os.path


class BookSpider(CrawlSpider):
	name = 'Book'
	# alloweddomains = ['xx.com']
	# #starturls = ['http://www.xx.com/']
	# #rules = ( # Rule(SgmlLinkExtractor(allow=r'.html'), callback='parseitem', follow=True), #)

	def _init(self, start_url, output_dir="./", *args, *kwargs):
		super(BookSpider, self).__init(args, *kwargs)
		self.start_urls = []
		self.start_urls.append(start_url)
		self.output_dir = output_dir
		self.allowed_domains = map(self._get_domain, self.start_urls)

	def _get_domain(self, url):
		first_dot = url.find('.')

		if -1 == first_dot: return None
		first_slash = url.find('/', first_dot + 1)
		if -1 == first_slash: return url[first_dot + 1:]
		return url[first_dot + 1: first_slash]

	def parse(self, response):
		"""first Request return to fetch start_url"""

		self.parse_detail(response)
		yield Request(response.url, callback=self.parse_item)

	def parse_item(self, response):
		page_links = SgmlLinkExtractor(allow=r'.html').extract_links(response)

		""" iterate two times for BFS; one for DFS"""
		for link in page_links:
			yield Request(link.url, callback=self.parse_detail)
		for link in page_links:
			yield Request(link.url, callback=self.parse_item)

	def parse_detail(self, response):
		outputfile = self._rtouch(response.url)

		if not outputfile:
			log.msg("download %s fail" % response.url, level=log.WARNING, spider=self)
			return
		with open(outputfile, 'w') as f:
			f.write(response.body)
		log.msg("download file: %s" % outputfile, level=log.INFO, spider=self)

	def _rtouch(self, filepath):
		pos = filepath.find('://')

		if -1 != pos:
			filepath = filepath[pos + 3:]
		if ".html" != filepath[-5:]:
			filepath += "/index.html"
		opath = os.path.abspath(self.output_dir + "/" + filepath)
		basedir = os.path.dirname(opath)
		if not os.path.exists(basedir):
			try:
				os.makedirs(basedir)
			except Exception as msg:
				log.msg(msg, level=log.WARNING, spider=self)
				return None
			return opath
