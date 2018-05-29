from django.db import models

class ParsedNews(models.Model):
    url = models.CharField(max_length=200, unique=True, db_index=True)
    agency_name = models.CharField(max_length=200, db_index=True)
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    
class NewsEvent(models.Model):

    PLACE_STREET = 0
    PLACE_ORGANISATION = 1

    PLACES_CHOICES = (
        (PLACE_STREET, 'street'),
        (PLACE_ORGANISATION, 'organization'),
    )

    news = models.ForeignKey(ParsedNews, db_index=True, on_delete=models.PROTECT)
    coordinates = models.TextField(blank=False, default='')
    place = models.IntegerField(choices=PLACES_CHOICES)
    place_description = models.CharField(max_length=200)

    @staticmethod
    def get_choice(place_name: str):
        for choice in NewsEvent.PLACES_CHOICES:
            if choice[1].lower() == place_name.lower():
                return choice[0]

        raise NotImplementedError()
