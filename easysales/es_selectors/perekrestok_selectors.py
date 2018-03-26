# coding=utf-8

# Start urls.
#
URLS = ['https://www.perekrestok.ru/catalog']
URL_CORE = 'https://perekrestok.ru'

# Categiries.
#
CATEGORIES = '//a[@class="xf-catalog-categories__link"]/@href'
CATEGORIES_TEXT = '//span[@class="xf-catalog-categories__text"]/text()'
POST_CATEGORY = '//span[@class="xf-breadcrumbs__current"]/text()'
CURRENT_CATEGORY = '//h1[@class="xf-caption__title"]/text()'

ROOT_NODE = '//ul[@id="catalogItems"]'
ITEM = 'li/div[contains(@class, "xf-product")]'

# Item attributes.
#
NAME = 'div[@class="xf-product__title xf-product-title"]/a[@class="xf-product-\
title__link js-product__title"]/text()'
IMG = 'figure/a/img/@data-src'
NEW_PRICE = 'div/div[contains(@class, "xf-product-cost__current")]/@data-cost'
OLD_PRICE = 'div/div[contains(@class, "xf-price xf-product-cost__prev")]/@data-cost'

# Pagination selector.
#
# next_page = '//li[@class="next"]/a/@href'
NEXT_PAGE = '//a[contains(@class, "xf-paginator__item js-paginator__next")]/@href'


# EOF

