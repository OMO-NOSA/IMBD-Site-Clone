from django.shortcuts import render
from core.models import Movie, Person,Role
from django.views.generic import (DetailView,
                                             ListView)
# Create your views here

class MovieListView(ListView):
    model = Movie
    
class MovieDetailView(DetailView):
    queryset = (
        Movie.objects.all_with_related_persons()
    )

class PersonDetailView(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()