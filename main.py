from scrapy.cmdline import execute
import sys
import os

path = os.path.dirname(__file__)
sys.path.insert(0, path)
execute(['scrapy', 'crawl', 'crawl_user'])