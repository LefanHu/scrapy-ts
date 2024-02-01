# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PeppaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class TaylorItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    title = scrapy.Field()
    board = scrapy.Field()
    description = scrapy.Field()
