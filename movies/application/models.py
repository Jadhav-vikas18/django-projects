from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class tollywood(models.Model):
    movie_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images/')
    trailer = models.URLField(max_length=500,default=True)
    date_of_release = models.DateField()
    actress= models.CharField(max_length=100,default=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    collections = models.PositiveIntegerField()

    def __str__(self):
        return self.movie_name
