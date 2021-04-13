from django.contrib import admin
from .models import Film, Info, Rating, Actors


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'imdb_rating', 'year']
    list_filter = ['year', 'imdb_rating']
    search_fields = ['title']

admin.site.register(Info)
admin.site.register(Rating)
admin.site.register(Actors)