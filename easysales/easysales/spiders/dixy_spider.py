# coding=utf-8

import scrapy
import sys
from time import time, gmtime, strftime
from json import dumps
import requests

from selectors import dixy_selectors as sel
from processors import text_processor as proc


class DixySpider(scrapy.Spider):
    name = 'dixy'
    start_urls = sel.URLS
    headers = {'Content-Type': 'application/json'}

    def parse(self, response):
        for item in response.xpath(sel.ITEM):
            json_data = {
                'shopId': 1,
                'name': proc.process(item.xpath(sel.NAME).extract_first()),
                'category': proc.process(item.xpath(sel.CATEGORY).extract_first()),
                'imageUrl': sel.URL_CORE + item.xpath(sel.IMG).extract_first(),
                'oldPrice': proc.concat(item.xpath(sel.OLD_PRICE_LEFT).extract_first(default='0'),
                    item.xpath(sel.OLD_PRICE_RIGHT).extract_first(default='0'), '.'),
                'newPrice': proc.concat(item.xpath(sel.NEW_PRICE_LEFT).extract_first(default='0'),
                    item.xpath(sel.NEW_PRICE_RIGHT).extract_first(default='0'), '.'),
                'discount': proc.process(item.xpath(sel.DISCOUNT).extract_first()),
                'dateIn': proc.split_by(proc.process(item.xpath(sel.DATE).extract_first()), '-')[0],
                'dateIn': proc.parse_date_in(item.xpath(sel.DATE).extract_first()),
                'dateOut': proc.parse_date_out(item.xpath(sel.DATE).extract_first()),
                'crawlDate': strftime('%Y-%m-%d', gmtime()),
                'condition': proc.process(item.xpath(sel.CONDITION).extract_first(default='-')),
            }

            # requests.post('http://46.17.44.125:8080/api/shops/', data=dumps(json_data), headers=self.headers)
            yield json_data

        next_page = response.xpath(sel.NEXT_PAGE).extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)


# EOF

