import scrapy
from scrapy.item import Item, Field
from yandex_investments.items import YandexInvestmentsStock


class StockCatalogSpider(scrapy.Spider):
    name = 'stock_catalog'
    start_urls = ['https://invest.yandex.ru/catalog/stock/']

    def parse(self, response):
        for stock in response.xpath(
                "//a[@class='lBT6RuJRjtvzChEJ_G30 yDtbhftw9A4mXqH3vPkH ZPgoa_UnfWgowwkvsp64 N9w__d8iYPl6C0KewYiA']"):
            item = YandexInvestmentsStock()
            item['name'] = stock.xpath(".//div[@class='tJYWSxg23zNUv79hPvVS']/text()").get()
            item['risk'] = stock.xpath(".//span[@class='oiTIR_Sf1_ObNUZhdLv5 mhSVC_KCosmKJ73T2s6O']/text()").get()
            item['price'] = stock.xpath(".//div[@class='JGT__mSaFfXxcOb2oGto']/text()").get()
            yield item
