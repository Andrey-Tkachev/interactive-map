import scrapy

class AdressFact(scrapy.Item):
    alias = 'simple_fact'
    Name = scrapy.Field()

    def from_dict(self, fact_dict, field_key=None):
        for field in self.fields:
            if field in fact_dict:
                if field_key:
                    self[field] = fact_dict[field][field_key]
                else:
                    self[field] = fact_dict[field]

class StreetFact(AdressFact):
    alias = 'street'
    Descr = scrapy.Field()

    def pretty_print(self):
        return str(self['Descr']) + " " + self['Name']

class OrgFact(AdressFact):
    alias = 'organization'
    Descr = scrapy.Field()

    def pretty_print(self):
        return str(self['Descr']) + " " + self['Name']
