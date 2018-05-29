import json
from django.http import (Http404, JsonResponse)
from django.core import serializers
from django.forms.models import model_to_dict
from django.shortcuts import render

from rest_framework import (serializers, viewsets)

from interactive_map.map_app.models import ParsedNews, NewsEvent

class EventsSerializer(serializers.ModelSerializer):
    news_title = serializers.ReadOnlyField(source='news.title')
    news_url= serializers.ReadOnlyField(source='news.url')

    class Meta:
        model = NewsEvent
        fields = ('news_title', 'news_url', 'coordinates')


class EventsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = NewsEvent.objects.all()
    serializer_class = EventsSerializer



def map_page(request):
    return render(request, 'index.html')
