# -*- coding: utf-8 -*-
import scrapy
from ..items import InvestItem


class BourseImoSpider(scrapy.Spider):
    name = 'BourseImoSpider'
    allowed_domains = ['bourse-immobilier.fr']
    start_urls = ['https://www.bourse-immobilier.fr/achat-appartement-acheres?quartiers=&surface=0&sterr=0&prix=-300000&typebien=2&nbpieces=2-3&og=0&where=Ach%c3%a8res-__78260_&_b=1&_p=1&tyloc=2&neuf=1&ancien=1&ids=78005/']

    def parse(self, response):
        all_properties = response.xpath(
            '//div[@class ="bien bien-bi  to-hover"]')

        for property in all_properties:
#            data = {}
#            data['title1'] = property.xpath(
#                './/div[@class = "bottom"]/a/span[@class = "ville"]/text()').extract_first()
#            data['title2'] = property.xpath(
#                './/div[@class = "bottom"]/a/span[@class = "description-1"]/text()').extract_first()
#            data['price'] = property.xpath(
#                './/div[@class = "bottom"]/a/span[@class = "prix"]/text()').extract_first()
#            print(data['title1'])
#            print(data['title2'])
#            print(data['price'])
#            yield data
            
            item = InvestItem()
            item['title'] = property.xpath(
                './/div[@class = "bottom"]/a/span[@class = "ville"]/text()').extract_first()
            item['size'] = property.xpath(
                './/div[@class = "bottom"]/a/span[@class = "description-1"]/text()').extract_first()
            item['price'] = property.xpath(
                './/div[@class = "bottom"]/a/span[@class = "prix"]/text()').extract_first()
            
            print(item['title'])
            print(item['size'])
            print(item['price'])
            
            yield item

            
            
