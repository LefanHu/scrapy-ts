# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from peppa.items import TaylorItem


class PeppaPipeline:
    def process_item(self, item: TaylorItem, spider):
        print(f"Downloading image: {item['url']}")

        
        return item
