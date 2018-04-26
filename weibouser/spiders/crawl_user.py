# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from ..items import WeibouserItem
from scrapy.selector import Selector
from ..util.create_url import GeneratorUrl
from ..util.get_logger import get_func_name
import logging
from datetime import datetime
from ..settings import WEIBO_API_HEADER
from scrapy.utils.project import get_project_settings
import json
import re
from redis import Redis
from ..settings import REDIS_DB, REDIS_HOST, REDIS_PORT, COOKIE_KEY_NAME

redis_connect = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True, db=REDIS_DB)


class CrawlUserSpider(scrapy.Spider):
    name = 'crawl_user'
    gen_url = GeneratorUrl()
    logger = logging.getLogger('{0}.{1}'.format(__name__, get_func_name()))
    setting = get_project_settings()

    def start_requests(self):
        for url in self.gen_url.get_hot_urls():
            yield Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        cookies_data = redis_connect.hgetall(COOKIE_KEY_NAME)
        try:
            cookies = json.loads(cookies_data['cookies'], encoding='utf-8')
        except KeyError:
            cookies = None
        except ValueError:
            cookies = None
            self.logger.info('JSON解析出错,删除cookies <DateTime %s>' % (datetime.now()))
            redis_connect.delete(COOKIE_KEY_NAME)
        self.logger.info('爬取热门首页 <status %s> <GET %s>' % (response.status, response.url))
        data = json.loads(response.text)
        text = data['data']
        mids = Selector(text=text).xpath('//div[@id="PCD_pictext_i_v5"]/ul/div/@mid').extract()
        for mid in mids:
            if re.match('^\d+:\d+', mid): continue
            url = self.gen_url.get_comment_urls(id_=mid)
            yield Request(url=url, callback=self.user_page_home, cookies=cookies)

    def user_page_home(self, response):
        self.logger.info('解析出每个文章首页评论列表 <status %s> <GET %s>' % (response.status, response.url))
        try:
            data = json.loads(response.text)['data']['html']
        except Exception, e:
            self.logger.info('解析失败 <Error %s> <GET %s>' % (e, response.url))
        else:
            users_message = Selector(text=data).xpath('//div[@node-type="comment_list"]//div[@class="WB_text"]/a[1]')
            for user_message in users_message:
                id = user_message.xpath('@usercard').extract_first('').encode('utf-8')
                name = user_message.xpath('text()').extract_first('').encode('utf-8')
                if not (id and name): continue
                id = id.strip('id=')
                url = self.gen_url.get_bigv_url(id=id, name=name)
                yield Request(url=url, callback=self.detail_page, headers=WEIBO_API_HEADER, meta={'user_name': name, 'user_id': id})

    def detail_page(self, response):
        json_data = json.loads(response.text)
        user_name = response.meta['user_name']
        try: card = json_data["cards"][0]
        except KeyError:
            self.logger.info('请求用户信息出错(昵称:%s) <URL %s>' % (user_name, response.url))
            return
        except IndexError:
            self.logger.info('过滤用户信息(昵称:%s) <URL %s>' % (user_name, response.url))
            return
        self.logger.info('解析用户信息(昵称:%s) <status %s> <GET %s>' % (user_name, response.status, response.url))
        time_flag = datetime.now()
        user_item = WeibouserItem()
        user = card["mblog"]["user"]
        user_item["name"] = user_name
        user_item["description"] = user.get("description", "")  # 描述
        user_item["user_create_at"] = user.get("created_at", "")  # 用户创建日期
        user_item["credit_score"] = user.get("credit_score", "")  # 信用评分
        user_item["followers_count"] = user.get("followers_count", 0)  # 粉丝数
        user_item["gender"] = user.get("gender", "")  # 性别（m）
        user_item["geo_enabled"] = user.get("geo_enabled", "")  # 是否认证
        user_id = response.meta['user_id']
        user_item["user_id"] = user_id  # user id
        user_item["location"] = user.get("location", "")  # 用户城市
        user_item["friends_count"] = user.get("friends_count", 0)  # 用户关注人数
        user_item["verified_level"] = user.get("verified_level", "")  # 认证级别
        user_item["statuses_count"] = user.get("statuses_count", 0)  # 全部微波数
        user_item["crawler_time"] = time_flag.strftime('%Y-%m-%d-%H')
        user_item['source'] = 'find_by_code'
        self.logger.info('用户信息写入item(昵称:%s)' % user_name)
        return user_item

