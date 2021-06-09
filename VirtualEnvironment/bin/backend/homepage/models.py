from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Movies(models.Model):
    identifier=models.CharField(max_length=100, null=True, blank=True)
    title=models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    poster = models.CharField(max_length=200)
    times = models.ForeignKey('Time', on_delete=PROTECT, null=True, blank=True)

    def __str__(self):
        return self.identifier

class Theatres(models.Model):
    identifier=models.CharField(max_length=100)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.identifier

class Time(models.Model):
    time=models.CharField(max_length=20, null=True, blank=True)
    movieID = models.CharField(max_length=100, null=True, blank=True)
    movie=models.ForeignKey(Movies, on_delete=PROTECT, null=True, blank=True)
    theatreID = models.CharField(max_length=100, null=True, blank=True)
    theatre=models.ForeignKey(Theatres, on_delete=PROTECT, null=True, blank=True)

    def __str__(self):
        return self.time






