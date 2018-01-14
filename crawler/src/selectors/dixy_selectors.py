#coding=utf-8

# Start urls.
#
urls = ['https://dixy.ru/akcii/skidki-nedeli']
url_core = 'https://dixy.ru'


# Item attributes.
#

# Root node.
#
item = '//div[contains(@class, "elem-product ")]'

# Inner repetitive divs.
#
description = 'div[@class="elem-product__description"]'
info = 'div[@class="elem-product__info"]'
price_container = info + '/div[@class="elem-product__price-container"]'
prices = price_container +'/div[@class="elem-product__prices"]'

img = info + '/div[@class="elem-product__image"]/img/@src'
name = description + '/div[contains(@class, "product-name")]/text()'
category = description + '/div[@class="product-category"]/child::text()[2]'
new_price_left = prices + '/div[@class="price-left"]/span/text()'
new_price_right = prices + '/div[@class="price-right"]/span/text()'
old_price_left = prices + '/div[@class="price-right"]/div/span[@class="price-full__integer"]/text()'
old_price_right = prices + '/div[@class="price-right"]/div/span[@class="price-full__float"]/text()'
discount = price_container + '/div[contains(@class,"discount")]/span[@class="value"]/text()' + ' | ' + price_container + '/div[@class="just-now"]/text()'
condition = price_container + '/div[contains(@class,"promopack")]/div[@class="text"]/text()'
date = 'div[contains(@class, "elem-badge-cornered")]/text()'


# Pagination selector.
#
next_page = '//li[@class="next"]/a/@href'


# EOF

