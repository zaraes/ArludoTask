from django.db import models

# Create your models here.
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="homepage/%y")
    def __str__(self):
        return self.caption

# class JSONExample(model.Model):
#     data = models.JSONField(default='')