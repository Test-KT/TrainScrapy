# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class TutorialItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass


class QuotesItem(scrapy.Item):
    title=scrapy.Field()
    author=scrapy.Field()
    tags=scrapy.Field()
    link=scrapy.Field()


class AuthorItem(scrapy.Item):
    name=scrapy.Field()
    date=scrapy.Field()
    desc=scrapy.Field()