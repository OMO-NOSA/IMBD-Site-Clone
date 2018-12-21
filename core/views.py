from django.shortcuts import render
from core.models import Movie
from django.views.generic import ListView
# Create your views here.

class MovieListView(ListView):
    model = Movie
    
