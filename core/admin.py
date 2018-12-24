from django.contrib import admin
from core.models import Movie,Person

# Model registrations are stacked here.

admin.site.register(Movie)
admin.site.register(Person)

