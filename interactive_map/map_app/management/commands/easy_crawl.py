from scrapy_app import crawl_spider
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Crawl news portals'
    
    def handle(self, *args, **options):
        crawl_spider('tass')
