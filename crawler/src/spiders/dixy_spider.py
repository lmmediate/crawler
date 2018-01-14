# coding=utf-8

import scrapy
import sys


# TODO: Fix relative paths.
#
sys.path.insert(0, './src/selectors/')
sys.path.insert(0, './src/processors/')
import dixy_selectors as sel
import text_processor as proc


class QuotesSpider(scrapy.Spider):
    name = 'dixy'
    start_urls = sel.urls

    def parse(self, response):
        for item in response.xpath(sel.item):
            yield {
                'name': proc.process(item.xpath(sel.name).extract_first()),
                'category': proc.process(item.xpath(sel.category).extract_first()),
                'img_url': sel.url_core + item.xpath(sel.img).extract_first(),
                'new_price': proc.concat(item.xpath(sel.new_price_left).extract_first(default='0'),
                    item.xpath(sel.new_price_right).extract_first(default='0'), '.'),
                'old_price': proc.concat(item.xpath(sel.old_price_left).extract_first(default='0'), 
                    item.xpath(sel.old_price_right).extract_first(default='0'), '.'),
                'discount': proc.process(item.xpath(sel.discount).extract_first()),
                'date': proc.process(item.xpath(sel.date).extract_first()),
                'condition': proc.process(item.xpath(sel.condition).extract_first(default='-')),
            }

        next_page = response.xpath(sel.next_page).extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)


# EOF

