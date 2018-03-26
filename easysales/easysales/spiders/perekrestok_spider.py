# coding=utf-8

import scrapy

from time import time, gmtime, strftime
from easysales.items import PerekrestokItem
from es_selectors import perekrestok_selectors as sel
from es_processors import text_processor as proc
# Python2 v Python3 compatibility trick.
#
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class PerekrestokSpider(scrapy.Spider):
    name = 'perekrestok'
    start_urls = sel.URLS

    def parse(self, response):
        categories_links = response.xpath(sel.CATEGORIES).extract()
        categories_links = categories_links[:len(categories_links)//2]
        for category in categories_links:
            url = urljoin(sel.URL_CORE, category)
            yield scrapy.Request(url=url, callback=self.parse_items)

    def parse_items(self, response):
        current_category = ''
        if 'post' in response.url:
            current_category = response.xpath(sel.POST_CATEGORY).extract_first()
        else:
            current_category = response.xpath(sel.CURRENT_CATEGORY).extract_first()
            current_category = proc.remove_junk(proc.split_by(current_category, '-')[0])

        items_count = len(response.xpath(sel.ROOT_NODE).xpath(sel.ITEM).extract())

        for item in response.xpath(sel.ROOT_NODE).xpath(sel.ITEM):
            pk_item = PerekrestokItem()
            pk_item['name'] = proc.remove_junk(item.xpath(sel.NAME).extract_first())
            pk_item['category'] = current_category
            pk_item['imageUrl'] = urljoin(sel.URL_CORE, item.xpath(sel.IMG).extract_first())
            pk_item['newPrice'] = proc.try_float(item.xpath(sel.NEW_PRICE).extract_first())
            pk_item['oldPrice'] = proc.try_float(item.xpath(sel.OLD_PRICE).extract_first(default=0))
            pk_item['crawlDate'] = strftime('%Y-%m-%d', gmtime())
            pk_item['shopId'] = 2
            yield pk_item

        next_page = response.xpath(sel.NEXT_PAGE).extract_first()

        if next_page is not None and items_count > 0:
            yield response.follow(next_page, self.parse_items)



# EOF

