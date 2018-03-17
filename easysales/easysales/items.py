import scrapy


class EasySalesItem(scrapy.Item):
    name = scrapy.Field()
    newPrice = scrapy.Field()
    imageUrl = scrapy.Field()
    shopId = scrapy.Field()
    crawlDate = scrapy.Field()


class DixyItem(EasySalesItem):
    category = scrapy.Field()
    oldPrice = scrapy.Field()
    discount = scrapy.Field()
    dateIn = scrapy.Field()
    dateOut = scrapy.Field()
    condition = scrapy.Field()

# EOF

