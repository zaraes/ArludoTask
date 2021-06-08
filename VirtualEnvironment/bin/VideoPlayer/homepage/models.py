from django.db import models
from django.db.models.deletion import PROTECT

# Create your models here.
class Time(models.Model):
    time1=models.CharField(max_length=20, null=True, blank=True)
    time2=models.CharField(max_length=20, null=True, blank=True)
    time3=models.CharField(max_length=20, null=True, blank=True)
    time4=models.CharField(max_length=20, null=True, blank=True)
    time5=models.CharField(max_length=20, null=True, blank=True)
    time6=models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.time

class Showtimes(models.Model):
    movie_identifer = models.CharField(max_length=100, null=True, blank=True)
    times=models.ForeignKey(Time, on_delete=PROTECT, null=True, blank=True)

    def initialise_times(self, Time):
        times = Time

    def __str__(self):
        return self.movie_identifer

class Movies(models.Model):
    identifier=models.CharField(max_length=100, null=True, blank=True)
    title=models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    poster = models.CharField(max_length=200)
    show_times = models.ForeignKey(Showtimes, on_delete=PROTECT, null=True, blank=True)

    def initialise_show_times(self, ShowTimes):
        show_times = Showtimes

    def __str__(self):
        return self.identifier

class Theatres(models.Model):
    identifier=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    showtimes=models.ForeignKey(Showtimes, on_delete=PROTECT, null=True, blank=True)

    def initialise_show_times(self, ShowTimes):
        showtimes = ShowTimes

    def __str__(self):
        return self.identifier






