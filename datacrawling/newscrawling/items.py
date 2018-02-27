import scrapy


class NewscrawlingItem(scrapy.Item):
    url = scrapy.Field()
    raw_text = scrapy.Field()
    date = scrapy.Field()
