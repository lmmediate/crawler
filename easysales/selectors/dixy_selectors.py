# coding=utf-8

# Start urls.
#
URLS = ['https://dixy.ru/akcii/skidki-nedeli']
URL_CORE = 'https://dixy.ru'


# Item attributes.
#

# Root node.
#
ITEM = '//div[contains(@class, "elem-product ")]'

# Inner repetitive divs.
#
DESCRIPTION = 'div[@class="elem-product__description"]'
INFO = 'div[@class="elem-product__info"]'
PRICE_CONTAINER = INFO + '/div[@class="elem-product__price-container"]'
PRICES = PRICE_CONTAINER + '/div[@class="elem-product__prices"]'

IMG = INFO + '/div[@class="elem-product__image"]/img/@src'
NAME = DESCRIPTION + '/div[contains(@class, "product-name")]/text()'
CATEGORY = DESCRIPTION + '/div[@class="product-category"]/child::text()[2]'
NEW_PRICE_LEFT = PRICES + '/div[@class="price-left"]/span/text()'
NEW_PRICE_RIGHT = PRICES + '/div[@class="price-right"]/span/text()'
OLD_PRICE_LEFT = PRICES + '/div[@class="price-right"]/div/span[@class="price-f\
ull__integer"]/text()'
OLD_PRICE_RIGHT = PRICES + '/div[@class="price-right"]/div/span[@class="price-\
full__float"]/text()'
DISCOUNT = PRICE_CONTAINER + '/div[contains(@class,"discount")]/span[@class="v\
alue"]/text()' + ' | ' + PRICE_CONTAINER + '/div[@class="just-now"]/text()'
CONDITION = PRICE_CONTAINER + '/div[contains(@class,"promopack")]/div[@class="\
text"]/text()'
DATE = 'div[contains(@class, "elem-badge-cornered")]/text()'

# Pagination selector.
#
# next_page = '//li[@class="next"]/a/@href'
NEXT_PAGE = '//div[contains(@class, "elem-pagination")]/a[contains(@class, "el\
em-pagination__btn--next")]/@href'

# EOF

