# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import re
import os
import json
import requests
from items import DixyItem
from config import const


class GeneralProcessPipeline(object):

    def process_item(self, item, spider):
        # Do post request for adding an item to the DB here.
        #
        item_ret = DixyItem()
        for k, v in dict(item).items():
            item_ret[k] = item[k][0]
        return item_ret


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.json', 'w')
        self.file.write('[')

    def close_spider(self, spider):
        self.file.close()
        self.file = open('items.json', 'r+')
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

