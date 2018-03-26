# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import os
import json
import requests
from config import const


class GeneralProcessPipeline(object):

    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open(const['URI_JSON_OUT'], 'w')
        self.file.write('[')

    def close_spider(self, spider):
        self.file.close()
        self.file = open(const['URI_JSON_OUT'], 'r+')
        data = self.file.read()
        self.file.seek(0)
        self.file.write(data[:-2])
        self.file.write(']\n')
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + ",\n"
        self.file.write(line)
        return item


class DataBaseWriterPipeLine(object):

    def process_item(self, item, spider):
        requests.post(const['ADD_ITEM_API'],
                      data=json.dumps(dict(item)),
                      headers=const['REQUEST_HEADERS'])
        return item

# EOF

