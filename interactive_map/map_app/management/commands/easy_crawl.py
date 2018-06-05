from django.core.management.base import BaseCommand, CommandError

from scrapy_app import crawl_spider


class Command(BaseCommand):
    help = 'Crawl news portals'
    
    def handle(self, *args, **options):
        crawl_spider('tass')
