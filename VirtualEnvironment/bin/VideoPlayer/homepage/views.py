import json

from django.shortcuts import *
from .models import Movies
from django.http import JsonResponse, HttpResponse


# Create your views here.
path = '/Users/zara/Arludo/VirtualEnvironment/bin/VideoPlayer/data/movie_metadata.json'
 
# def read_file(path):
#     file = open(path, "r")
#     data = file.read()
#     file.close()
#     return data

# def read_json(path):
#     return json.loads(read_file(path))

# def return_json(request):
#     return read_json(path)

def index(request):
    movie = Movies.objects.all()
    return render(request, "index.html", {"movie": movie})
    




    

