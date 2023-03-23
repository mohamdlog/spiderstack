# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryItem(scrapy.Item):
    country_name = scrapy.Field()
    country_capital = scrapy.Field()
    country_population = scrapy.Field()
    country_area = scrapy.Field()