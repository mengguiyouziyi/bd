#coding:utf-8
import os
import sys

from scrapy.cmdline import execute

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
sys.path.append(path)

execute(['scrapy', 'crawl', 'bk'])