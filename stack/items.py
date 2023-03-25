# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FinanceItem(scrapy.Item):
    stock_name = scrapy.Field()
    previous_close = scrapy.Field()
    open = scrapy.Field()
    bid = scrapy.Field()
    ask = scrapy.Field()
    range_day = scrapy.Field()
    range_52weeks = scrapy.Field()
    volume = scrapy.Field()
    avg_volume = scrapy.Field()