from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('movies', views.MovieListView.as_view(), name='MovieList'), 
    path('movie/<int:pk>', views.MovieDetailView.as_view(), name='MovieDetail'),
    path('person', views.PersonDetailView.as_view(), name='PersonDetail'),

]