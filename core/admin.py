from django.contrib import admin
from core.models import Movie,Person,Role,Vote,MovieImage

# Model registrations are stacked here.

admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Vote)
admin.site.register(MovieImage)

