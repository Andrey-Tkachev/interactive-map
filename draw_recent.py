import json
import pprint

import random
import requests

import global_settings
import pymongo
import scrapy
from textmeaning import facttypes as ft
from textmeaning import TomitaExtracter


def addressToPoint(address):
    url = 'https://geocode-maps.yandex.ru/1.x/?format=json&geocode=Москва,+{}'.format(address)
    req = requests.get(url)
    d = json.loads(req.text)
    if len(d['response']['GeoObjectCollection']['featureMember']) != 0:
        coordinates = d['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'] # e.g. 37.611347 55.760241
        return coordinates.replace(" ", ",")
    return None

def constructMapURL(points):
    params = []
    for coordinate in points:
        params.append('{},pm2{}m'.format(coordinate, random.choice(['gn', 'rd', 'yw'])))

    return 'https://static-maps.yandex.ru/1.x/?l=map&pt={}'.format('~'.join(params))


if __name__ == '__main__':
    client = pymongo.MongoClient(global_settings.MONGO_URI)
    db = client[global_settings.MONGO_DB]
    collection = db[global_settings.MONGO_RNEWS_COLLECTION]

    places = []
    te = TomitaExtracter(tomita_env='./tomita', tomita_bin=global_settings.TOMITA_BIN)
    news = collection.find({})
    for ind, raw_news in enumerate(news):
        print('Current url: ', raw_news['url'])
        facts = te.extract(raw_news['raw_text'], facttypes_to_extract=[ft.StreetFact, ft.OrgFact])
        if (len(facts) != 0):
            for facttype in facts:
                for fact in facts[facttype]:
                    places.append(fact.pretty_print())

    points = []
    for place in places:
        address = addressToPoint(place)
        if address is not None:
            points.append(addressToPoint(place))
        else:
            print('Not found: ' + place)

    print(constructMapURL(points))
