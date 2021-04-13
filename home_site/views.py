from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film, Info, Rating
from .forms import FilmForm, InfoForm, RatingForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from .serializers import UserSerializer, FilmSerializer
from django.contrib.auth.models import User


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class FilmView(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


def film_titles(request):
    all_films = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': all_films})

@login_required
def new_film(request):
    form = FilmForm(request.POST or None, request.FILES or None)
    form_info = InfoForm(request.POST or None)

    if all((form.is_valid(), form_info.is_valid())):
        film = form.save(commit = False)
        add_info = form_info.save()
        film.add_info = add_info
        film.save()
        return redirect(film_titles)

    return render(request, 'film_form.html', {'form': form, 'form_info': form_info, 'new': True})

@login_required
def edit_film(request, id):
    film = get_object_or_404(Film, pk = id)
    rate = Rating.objects.filter(movie = film)

    try:    
        film_add = Info.objects.get(film = film.id)

    except Info.DoesNotExist:
        film_add = None

    form = FilmForm(request.POST or None, request.FILES or None, instance = film)
    form_add = InfoForm(request.POST or None,  instance = film_add)
    form_rate = RatingForm(request.POST or None)

    if request.method == 'POST':
        if 'review' in request.POST:
            new_rate = form_rate.save(commit = False)
            new_rate.movie = film
            new_rate.save()

    if all((form.is_valid(), form_add.is_valid())):
        film = form.save(commit = False)
        add_info = form_add.save()
        film.add_info = add_info
        film.save()
        return redirect(film_titles)

    return render(request, 'film_form.html', {'form': form, 'form_info': form_add, 'form_rate': form_rate, 'rate': rate, 'new': False})

@login_required
def delete_film(request, id):
    film = get_object_or_404(Film, pk = id)

    if request.method == 'POST':
        film.delete()
        return redirect(film_titles)

    return render(request, 'confirm.html', {'film': film})