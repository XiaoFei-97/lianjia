# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lianjia.items import LianjiaItem


class ZufangSpider(CrawlSpider):
    name = 'zufang'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://hz.lianjia.com/zufang/']

    rules = (
        Rule(LinkExtractor(allow=r'zufang/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        for each in response.xpath('//li[@data-el="zufang"]/div[@class="info-panel"]'):

            item = LianjiaItem()

            item["title"] = each.xpath('//h2/a/text()').extract()[0]
            item["link"] = each.xpath('//h2/a/@href').extract()[0]
            item["address"] = each.xpath('//div[@class="where"]/a/span/text()').extract()[0].replace('\xa0\xa0', '')
            item["zone"] = each.xpath('//div[@class="where"]/span[@class="zone"]/span/text()').extract()[0].replace('\xa0\xa0', '')
            item["meters"] = each.xpath('//div[@class="where"]/span[@class="meters"]/text()').extract()[0].replace('\xa0\xa0', '')[:-2]
            item["direction"] = each.xpath('//div[@class="where"]/span[3]/text()').extract()[0]
            item["price"] = each.xpath('//div[@class="price"]/span/text()').extract()[0]
            item["update_date"] = each.xpath( '//div[@class="price-pre"]/text()').extract()[0][:-2]
            item["num"] = each.xpath('//div[@class="square"]//span[@class="num"]/text()').extract()[0]
            item["other"] = each.xpath('string(//div[@class="con"])').extract()[0]

            yield item

