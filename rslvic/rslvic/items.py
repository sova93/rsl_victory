import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class RslvicItem(scrapy.Item):
    item = scrapy.Field()


class RslvicItemLoader(ItemLoader):
    item_out = TakeFirst()