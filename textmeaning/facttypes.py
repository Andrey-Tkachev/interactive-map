import scrapy

class AdressFact(scrapy.Item):
    Name = scrapy.Field()

    def from_dict(self, fact_dict, field_key=None):
        for field in self.fields:
            if field in fact_dict:
                if field_key:
                    self[field] = fact_dict[field][field_key]
                else:
                    self[field] = fact_dict[field]

class StreetFact(AdressFact):
    Descr = scrapy.Field()

class OrgFact(AdressFact):
    Descr = scrapy.Field()
