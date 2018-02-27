from textmeaning.facts_extracters import TomitaExtracter
from textmeaning import facttypes as ft

import scrapy
import pprint

te = TomitaExtracter(tomita_env='./tomita', tomita_bin='./bin/tomita-linux64')
test_news = open('./test_news/n1.txt', 'r')
data = ''.join(test_news.readlines())
pprint.pprint(te.extract(data, fact_types=[ft.StreetFact]))