import json
import pprint

import random
import requests

from django.core.management.base import BaseCommand, CommandError
from interactive_map.map_app.models import ParsedNews, NewsEvent

import pymongo
import scrapy

import global_settings
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


class Command(BaseCommand):
    help = 'Extract places from raw news'

    def handle(self, *args, **options):
        client = pymongo.MongoClient(global_settings.MONGO_URI)
        db = client[global_settings.MONGO_SCRAPY_DB]
        collection = db[global_settings.MONGO_CRAWLED_COLLECTION]

        places = []
        te = TomitaExtracter(tomita_env='./tomita_env', tomita_bin=global_settings.TOMITA_BIN)
        news = collection.find({})
        self.stdout.write(global_settings.MONGO_CRAWLED_COLLECTION)

        for ind, raw_news in enumerate(news):
            if not raw_news['raw_text'] or not raw_news['title']:
                self.stdout.write(self.style.NOTICE('Bad url: ' + raw_news['url']))
                continue

            news, _ = ParsedNews.objects.update_or_create(url=raw_news['url'],
                                                       defaults= {
                                                           'agency_name': raw_news.get('agency_name', 'tass'),
                                                           'title': raw_news['title'],
                                                        })

            facts = te.extract(raw_news['raw_text'], facttypes_to_extract=[ft.StreetFact, ft.OrgFact])
            if (len(facts) != 0):
                for fact in facts:
                    fact_point = addressToPoint(fact.pretty_print())
                    if fact_point is None:
                        self.stdout.write(self.style.NOTICE('Empty coordinates: ' + fact.pretty_print()))
                        continue

                    django_place_type = NewsEvent.get_choice(fact.alias)
                    description = fact.pretty_print()
                    NewsEvent.objects.create(news=news,
                                             place=django_place_type,
                                             coordinates=fact_point,
                                             place_description=description)

            self.stdout.write(self.style.WARNING('Processed url: ' + raw_news['url']))

        points = []
        for place in places:
            address = addressToPoint(place)
            if address is not None:
                points.append(addressToPoint(place))
            else:
                self.stdout.write(self.style.ERROR('Not found: ' + place))

        self.stdout.write(self.style.SUCCESS(constructMapURL(points)))
