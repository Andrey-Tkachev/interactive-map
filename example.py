from textmeaning.facts_extracters import TomitaExtracter
from textmeaning import facttypes as ft

import global_settings
import scrapy
import pprint
import pymongo


if __name__ == '__main__':
    client = pymongo.MongoClient(global_settings.MONGO_URI)
    db = client[global_settings.MONGO_DB]
    collection = db[global_settings.MONGO_RNEWS_COLLECTION]

    te = TomitaExtracter(tomita_env='./tomita', tomita_bin='./bin/tomita-linux64')    
    for raw_news in collection.find({}):
        facts = te.extract(raw_news['raw_text'], fact_types=[ft.StreetFact, ft.OrgFact])
        if (len(facts) != 0):
            pprint.pprint(raw_news['url'])
            for fact_type in facts:
                pprint.pprint(facts[fact_type])
