# coding=utf-8

import scrapy
import sys
import requests

from time import time, sleep, gmtime, strftime
from json import dumps
from easysales.items import DixyItem
from es_selectors import dixy_selectors as sel
from es_processors import text_processor as proc


class DixySpider(scrapy.Spider):
    name = 'dixy'
    start_urls = sel.URLS
    d_categs = {}

    def parse(self, response):
        categories = response.xpath(sel.CATEGORY_ID).extract()
        categories_names = response.xpath(sel.CATEGORY_NAME).extract()[1:]
        self.d_categs = dict(zip(categories, categories_names))
        print(self.d_categs)
        for c in categories:
            url = sel.URLS[0] + '?category=' + c
            sleep(0.5)
            yield scrapy.Request(url, callback=self.after_parse, dont_filter=True)
        sleep(1)
        yield scrapy.Request(sel.URLS[0] + sel.DAY_ITEM_QUERY, callback=self.after_parse, dont_filter=True)

    def after_parse(self, response):
        for item in response.xpath(sel.ITEM):
            dixy_item = DixyItem()
            dixy_item['shopId'] = 1
            dixy_item['name'] = proc.process(item.xpath(sel.NAME).extract_first())
            # dixy_item['category'] = proc.process(item.xpath(sel.CATEGORY).extract_first())
            categ = response.url[-3:]
            print response.url
            if categ != sel.DAY_ITEM_QUERY[-3:]:
                dixy_item['category'] = proc.process(self.d_categs[categ])
            else:
                dixy_item['category'] = sel.DAY_ITEM
            dixy_item['imageUrl'] = sel.URL_CORE + item.xpath(sel.IMG).extract_first()
            dixy_item['oldPrice'] = proc.concat(item.xpath(sel.OLD_PRICE_LEFT).extract_first(default='0'),
                item.xpath(sel.OLD_PRICE_RIGHT).extract_first(default='0'), '.')
            dixy_item['newPrice'] = proc.concat(item.xpath(sel.NEW_PRICE_LEFT).extract_first(default='0'),
                item.xpath(sel.NEW_PRICE_RIGHT).extract_first(default='0'), '.')
            dixy_item['discount'] = proc.process_str(item.xpath(sel.DISCOUNT).extract_first())
            dixy_item['dateIn'] = proc.split_by(proc.process(item.xpath(sel.DATE).extract_first()), '-')[0]
            dixy_item['dateIn'] = proc.parse_date_in(item.xpath(sel.DATE).extract_first())
            dixy_item['dateOut'] = proc.parse_date_out(item.xpath(sel.DATE).extract_first())
            dixy_item['crawlDate'] = strftime('%Y-%m-%d', gmtime())
            dixy_item['condition'] = proc.process(item.xpath(sel.CONDITION).extract_first(default='-'))

            yield dixy_item

        next_page = response.xpath(sel.NEXT_PAGE).extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)


# EOF

