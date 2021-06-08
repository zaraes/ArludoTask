from django.db import models

# Create your models here.
class Movies(models.Model):
    id=models.CharField(max_length=100, primary_key=True)
    title=models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    poster = models.CharField(max_length=200)

    # def __str__(self):
    #     return f'{self.id}, {self.title}, {self.rating}, {self.poster}' 

# class JSONExample(model.Model):
#     data = models.JSONField(default='')