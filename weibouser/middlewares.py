# -*- coding: utf-8 -*-


from scrapy import signals
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from scrapy.downloadermiddlewares.redirect import RedirectMiddleware
import random
from util.get_logger import get_func_name
from scrapy import Request
from settings import GET_COOKIE_URL, REDIS_DB, REDIS_HOST, REDIS_PORT, COOKIE_KEY_NAME
from redis import Redis
import requests
from datetime import datetime, timedelta
import logging
import json
from pickle import dumps, loads
from scrapy.exceptions import IgnoreRequest

redis_connect = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, db=REDIS_DB)


class RandomUserAgentMiddleware(UserAgentMiddleware):
    def __init__(self, user_agent_list):
        self.user_agent_list = user_agent_list

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent_list=crawler.settings.get('USER_AGENT')
        )

    def process_request(self, request, spider):
        random_user_agent = random.choice(self.user_agent_list)
        request.headers.setdefault('User-Agent', random_user_agent)


class ProxyMiddleware(object):
    def __init__(self):
        self.proxy_list = [
                      ]

    def process_request(self, request, spider):
        random_ip = random.choice(self.proxy_list)
        request.meta['proxy'] = random_ip


class CustomRedirectMiddleware(RedirectMiddleware):
    logger = logging.getLogger('{0}.{1}'.format(__name__, get_func_name()))

    def process_response(self, request, response, spider):
        not_allow_redict_codes = {301, 302}
        if response.status in not_allow_redict_codes:
            set_time = redis_connect.hget('cookies_data', 'set_time')
            try:
                delta = datetime.now() - loads(set_time)
                print delta
                if delta < timedelta(seconds=60): return response
            except TypeError:
                self.logger.info('初始化Cookie,并设置初始化时间 <status %s><DateTime %s>' % (
                    response.status, datetime.now().strftime('%y-%m-%d-%H-%M')))
            cookies = json.dumps(self.get_new_cookies())
            if cookies:
                self.logger.info('Cookie失效,重新获取Cookie <status %s><DateTime %s>' % (
                response.status, datetime.now().strftime('%y-%m-%d-%H-%M')))
                redis_connect.hmset(COOKIE_KEY_NAME, {'cookies': cookies, 'set_time': dumps(datetime.now())})
            else:
                self.logger.warning(
                    'Cookie获取失败,Cookie为空 <DateTime %s>' % (datetime.now().strftime('%y-%m-%d-%H-%M')))
                # TODO: cookies 连接可能失效，发送邮件
            self.logger.info('重新爬取未成功的url <GET %s>' % request.url)
            return Request(url=request.url, cookies=cookies, dont_filter=True, callback=spider.user_page_home)
        return response

    def get_new_cookies(self):
        response = requests.get(GET_COOKIE_URL)
        return response.cookies.get_dict()


if __name__ == '__main__':
    from scrapy.utils.project import get_project_settings
    settings = get_project_settings()
    settings.set('TEST', 'r')
    print settings.get('TEST')







