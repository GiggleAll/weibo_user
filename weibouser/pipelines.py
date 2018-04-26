# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import WeibouserItem
from datetime import datetime
from util.get_logger import get_func_name
import os
import json
import logging

root_path = ''


class WeibouserPipeline(object):
    logger = logging.getLogger('{0}.{1}'.format(__name__, get_func_name()))

    def process_item(self, item, spider):
        stock_path = datetime.now().strftime('%Y-%m-%d-%Hh')
        USER_PATH = os.path.join(root_path,'{0}_stock_user.json'.format(stock_path))
        with open(USER_PATH, 'a') as fl:
            fl.write('sina_user {0}\n'.format(json.dumps(dict(item))))
        self.logger.info('用户信息写入文件, <PATH %s>' % USER_PATH)
        return item
