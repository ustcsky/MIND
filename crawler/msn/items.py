# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class NewsItem(scrapy.Item):
    nid = scrapy.Field()
    title = scrapy.Field()
    body = scrapy.Field() 
    vert = scrapy.Field() 
    subvert = scrapy.Field() 
    pass

