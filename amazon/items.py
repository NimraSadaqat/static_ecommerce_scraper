# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:

    no = scrapy.Field()
    title = scrapy.Field()
    asin = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    pass
