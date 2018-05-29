from django.contrib import admin
from .models import ParsedNews, NewsEvent

@admin.register(ParsedNews)
class ParsedNewsAdmin(admin.ModelAdmin):
    list_display = ('agency_name', 'title', 'url')

@admin.register(NewsEvent)
class NewsEventAdmin(admin.ModelAdmin):
    list_display = ('news', 'news_title',
                    'place', 'coordinates', 'place_description')

    def news_title(self, obj):
        return obj.news.title
