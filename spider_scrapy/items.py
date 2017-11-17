# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderScrapyItem(scrapy.Item):
    # 项目标题
    title = scrapy.Field()
    # 项目编号
    code = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 发布时间
    createTime = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 页面URL
    url = scrapy.Field()
