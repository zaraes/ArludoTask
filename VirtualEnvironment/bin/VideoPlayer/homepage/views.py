from django.shortcuts import render
from .models import Video
# import requests
from django.http import JsonResponse

API_KEY = 1

# Create your views here.
def index(request):
    video=Video.objects.all()
    return render(request, "index.html", {"video": video})
