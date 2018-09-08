# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # 租房标题
    title = scrapy.Field()
    # 租房链接
    link = scrapy.Field()
    # 租房地址
    address = scrapy.Field()
    # 租房户型
    zone = scrapy.Field()
    # 租房大小
    meters = scrapy.Field()
    # 租房朝向
    direction = scrapy.Field()
    # 房屋价格
    price = scrapy.Field()
    # 更新日期
    update_date = scrapy.Field()
    # 看房人数
    num = scrapy.Field()
    # 其他信息
    other = scrapy.Field()

