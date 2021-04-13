from django.urls import path
from .views import film_titles, new_film, edit_film, delete_film

urlpatterns = [
    path('titles/', film_titles, name = 'film_titles'),
    path('new/', new_film, name = 'new_film'),
    path('edit/<int:id>/', edit_film, name = 'edit_film'),
    path('delete/<int:id>/', delete_film, name = 'delete_film'),
]