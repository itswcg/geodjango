from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from .models import People


@admin.register(People)
class PeopleAdmin(OSMGeoAdmin):
    list_display = ('username', 'sex', 'age', 'location')
