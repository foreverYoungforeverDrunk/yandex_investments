import scrapy


class YandexInvestmentsStock(scrapy.Item):
    name = scrapy.Field()
    risk = scrapy.Field()
    price = scrapy.Field()
