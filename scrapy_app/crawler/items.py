import scrapy


class NewscrawlingItem(scrapy.Item):
    url = scrapy.Field()
    title = scrapy.Field()
    raw_text = scrapy.Field()
    agency = scrapy.Field()
    date = scrapy.Field()
