# -*- coding: utf-8 -*-

BOT_NAME = 'weibouser'
SPIDER_MODULES = ['weibouser.spiders']
NEWSPIDER_MODULE = 'weibouser.spiders'

USER_AGENT = [
    'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17',
    'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36',
    'Mozilla/5.0 (X11; OpenBSD i386) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36',
    'Mozilla/5.0 (X11; NetBSD) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.116 Safari/537.36,',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0',
]
ROBOTSTXT_OBEY = False
CONCURRENT_REQUESTS = 8
DOWNLOAD_DELAY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 8
REFERER_ENABLED = True
DOWNLOAD_TIMEOUT = 10
RETRY_TIMES = 3
RETRY_HTTP_CODES = [403]
TELNETCONSOLE_ENABLED = False

COOKIES_DEBIG = True
COOKIES_ENABLED = True
LOG_LEVEL = 'INFO'
GET_COOKIE_URL = 'https://login.sina.com.cn/visitor/visitor?a=crossdomain&cb=return_back&s=_2AkMt4Wm7f8NxqwJRmPkWzm3rZI9zyAvEieKbvZhgJRMxHRl-yj9jqk8HtRB6BmFHVAS8yeaHeXtJ4G3NrZ8YRWVu9MQb&sp=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFdTb81ZeCK8snOErWefUhP&from=weibo&_rand=0.9048780359784789'

DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Host': 'weibo.com',
    'Referer': 'https://weibo.com/?category=0',
}
WEIBO_API_HEADER = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'api.weibo.cn',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

# SPIDER_MIDDLEWARES = {
#    'weibouser.middlewares.WeibouserSpiderMiddleware': 543,
# }

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'weibouser.middlewares.RandomUserAgentMiddleware': 100,
    'weibouser.middlewares.CustomRedirectMiddleware': 601,
}

ITEM_PIPELINES = {
    'weibouser.pipelines.WeibouserPipeline': 300,
}

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 1
COOKIE_KEY_NAME = 'cookies_data'



