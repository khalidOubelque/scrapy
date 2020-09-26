# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy as sp


class InvestItem(sp.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = sp.Field() 
    propretyLink = sp.Field() 
    imageURL = sp.Field() 
    price = sp.Field() 
    size = sp.Field() 
    beedrooms = sp.Field() 
    type = sp.Field() 
    city = sp.Field() 
    pass
