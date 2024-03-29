from django.contrib import admin
from .models import Genre, Movie, Serie

# Register your models here.


#create classes to customize how admin displays models

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class MovieAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'release_year', 'title', 'genre', 'duration_min')

class SerieAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id', 'release_year', 'title', 'seasons', 'episodes', 'genre')


admin.site.register (Genre, GenreAdmin)
admin.site.register (Movie, MovieAdmin)
admin.site.register (Serie, SerieAdmin)
