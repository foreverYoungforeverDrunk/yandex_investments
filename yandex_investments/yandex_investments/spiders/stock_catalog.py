import scrapy


class StockCatalogSpider(scrapy.Spider):
    name = 'stock_catalog'
    allowed_domains = ['https://invest.yandex.ru/onboarding/']
    start_urls = ['http://https://invest.yandex.ru/onboarding//']

    def parse(self, response, **kwargs):
        pass
