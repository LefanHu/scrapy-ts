# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from peppa.items import TaylorItem
from peppa.spiders.taylor import TaylorSpider

import pandas

# class TaylorImageInfo:
#     image_url: str
#     width: int
#     height: int
#     board: str
#     title: str


class PeppaPipeline:
    def process_item(self, item: TaylorItem, spider: TaylorSpider):
        data = [
            item["title"],
            item["board"],
            item["description"],
            item["width"],
            item["height"],
            item["image_urls"],
            item["images"],
        ]
        spider.data.append(data)
        return item
