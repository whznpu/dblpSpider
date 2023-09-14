# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DblpItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    authors=scrapy.Field()
    year=scrapy.Field()
    conf=scrapy.Field()
    title=scrapy.Field()
    pass
