# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from newscrawling.items import NewscrawlingItem 

class TassSpider(CrawlSpider):
    name = 'tass'
    allowed_domains = ['tass.ru']
    start_urls = ['http://tass.ru/moskva']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[contains(@class, 'b-news-item__text')]/a"),
            callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = NewscrawlingItem()
        item['url'] = response.url
        item['raw_text'] = ''.join(response.xpath('//div[contains(@class, "b-material-text__l js-mediator-article")]/p/text()')
                                           .extract())
        item['date'] = response.xpath('//span[contains(@class, "b-material__date")]/text()')
                               .extract_first()

        return item
