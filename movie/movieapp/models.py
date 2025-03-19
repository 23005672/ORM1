from django.db import models
from django.contrib import admin
class Movie(models.Model):
    title = models.CharField(max_length=255, help_text="Movie Title")
    director = models.CharField(max_length=100, help_text="Director Name")
    release_date = models.DateField(help_text="Release Date")
    genre = models.CharField(max_length=50, help_text="Movie Genre")
    rating = models.DecimalField(max_digits=3, decimal_places=1, help_text="Movie Rating (e.g., 8.5)")
    duration = models.IntegerField(help_text="Duration in Minutes")

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'genre', 'rating', 'duration')