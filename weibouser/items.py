# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class WeibouserItem(scrapy.Item):
    name = Field()
    description = Field()
    user_create_at = Field()
    credit_score = Field()
    followers_count = Field()
    gender = Field()
    crawler_time = Field()
    geo_enabled = Field()
    user_id = Field()
    location = Field()
    friends_count = Field()
    verified_level = Field()
    statuses_count = Field()
    source = Field()

