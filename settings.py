import os

TOMITA_BIN = './bin/tomita-linux64'
MONGO_URI = os.environ.get('MONGO_URI')

MONGO_SCRAPY_DB = os.environ.get('MONGO_SCRAPY_DB')
MONGO_CRAWLED_COLLECTION = os.environ.get('MONGO_CRAWLED_COLLECTION')
