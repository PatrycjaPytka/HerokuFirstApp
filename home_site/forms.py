from django.forms import ModelForm
from .models import Film, Info, Rating, Actors

class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['title', 'about', 'premier_date', 'imdb_rating', 'plakat']

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = ['time', 'movie_type']

class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['review', 'stars']