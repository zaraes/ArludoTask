from django.contrib import admin

# Register your models here.
from .models import Movies, Theatres, Time
admin.site.register(Movies)
admin.site.register(Theatres)
admin.site.register(Time)