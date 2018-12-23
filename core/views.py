from django.shortcuts import render
from core.models import Movie
from django.views.generic import (DetailView,
                                             ListView)
# Create your views here

class MovieListView(ListView):
    model = Movie
    
class MovieDetailView(DetailView):
    model = Movie
