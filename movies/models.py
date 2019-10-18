from django.db import models

# Create your models here.
"""
    Charfield
    Int
    Float
    Boolean
"""

class Genre(models.Model):
    name = models.CharField(max_length=250)


    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    duration_min = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
