# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class SpiderTutorialItem(scrapy.Item):
    # define the fields for your item here like:
    country = scrapy.Field()
    year = scrapy.Field()
    population = scrapy.Field()

