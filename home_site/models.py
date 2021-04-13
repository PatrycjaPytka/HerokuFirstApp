from django.db import models


class Info(models.Model):
    types = {
        (0, 'Horror'),
        (1, 'Comedy'),
        (2, 'Drama'),
        (3, 'Sci-fi'),
        (4, 'Inne'),
    }
    time = models.PositiveSmallIntegerField(default = 0)
    movie_type = models.PositiveSmallIntegerField(default = 4, choices = types)


class Film(models.Model):
    title = models.CharField(max_length = 100, blank = False, unique = True)
    year = models.PositiveSmallIntegerField(default = 2000)
    about = models.TextField(default = 'None')
    premier_date = models.DateField(null = True, blank = True)
    imdb_rating = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)
    plakat = models.ImageField(upload_to = 'plakaty', null = True, blank = True)
    add_info = models.OneToOneField(Info, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.title_and_year()

    def title_and_year(self):
        return '{} ({})'.format(self.title, self.year)


class Rating(models.Model):
    review = models.TextField(default = "None", blank = True)
    stars = models.PositiveSmallIntegerField(default = 5)
    movie = models.ForeignKey(Film, on_delete = models.CASCADE)


class Actors(models.Model):
    name = models.CharField(max_length = 32)
    surname = models.CharField(max_length = 32)
    movies = models.ManyToManyField(Film, related_name = 'actors')
