import scrapy


class TaylorSpider(scrapy.Spider):
    name = "taylor"
    allowed_domains = ["pinterest.com"]
    start_urls = ["https://pinterest.com"]

    def parse(self, response):
        pass
