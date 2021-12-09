# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YandexInvestmentsStock(scrapy.Item):
    name = scrapy.Field()
    risk = scrapy.Field()
    price = scrapy.Field()
