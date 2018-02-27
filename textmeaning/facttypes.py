import scrapy

class AdressFact(scrapy.Item):
    Name = scrapy.Field()

    def from_dict(self, dict, field_key=None):
        for field in self.fields:
            if field in dict:
                if field_key:
                    self[field] = dict[field][field_key]
                else:
                    self[field] = dict[field]

class StreetFact(AdressFact):
    Descr = scrapy.Field()
