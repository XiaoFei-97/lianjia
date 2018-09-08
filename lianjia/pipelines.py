# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs


class LianjiaPipeline(object):
    def __init__(self):
        # 创建一个只写文件，指定文本编码格式为utf-8
        self.filename = codecs.open('zufang.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.filename.write(content)
        return item

    def spider_closed(self, spider):
        self.file.close()
