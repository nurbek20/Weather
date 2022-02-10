from django.contrib import admin
from weatherapp.models import SearchedCity
# Register your models here.
class SearchedCityAdmin(admin.ModelAdmin):
    list_display=('city', 'temperature', 'sent_at', 'updated')
    search_fields=['city']
    list_filter=('sent_at', 'updated')
    list_editable=['temperature']
    readonly_fields=['city', 'sent_at', 'updated']
admin.site.register(SearchedCity, SearchedCityAdmin)

# class WeatherAdmin(admin.ModelAdmin):
#     list_display=('icon')
# admin.site.register(Weather, WeatherAdmin)