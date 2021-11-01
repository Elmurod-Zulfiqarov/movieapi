from django.contrib import admin
from film.models import Movie, Actor, Comment

admin.site.register([Movie, Actor, Comment])

