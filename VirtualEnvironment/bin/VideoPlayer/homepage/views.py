import json

from django.shortcuts import *
from .models import Movies, Time, Showtimes, Theatres
from django.http import JsonResponse, HttpResponse


# Create your views here.
path_movies = '/Users/zara/Arludo/VirtualEnvironment/bin/VideoPlayer/data/movie_metadata.json'
path_showtimes = '/Users/zara/Arludo/VirtualEnvironment/bin/VideoPlayer/data/theater_showtimes.json'
 
def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def read_json(path):
    return json.loads(read_file(path))

def index(request):
    if Movies.objects.count() == 0:
        all_movies = read_json(path_movies)
        for i in all_movies:
            Movies.objects.create(identifier=i["id"], title=i["title"], rating=i["rating"], poster=i["poster"])
 

    all_theaters = read_json(path_showtimes)
    for i in all_theaters:
        print("id  =       " + str(i["id"]))
        print("name =      " + str(i["name"]))
        print("showtimes = ")
        TheatreObj = Theatres.objects.create(identifier = i["id"], name=i["name"], showtimes=None)
        for j in i["showtimes"]:
            print("movie ID: " + str(j))
            print("time: ")
            ShowTime_obj = Showtimes.objects.create(movie_identifer=j, times=None)
            print("j = " + str(j))

            TheatreObj.initialise_show_times(ShowTime_obj)
            
            for k in range(len(i["showtimes"][j])):
                print(i["showtimes"][j][k])
                # Time.objects.create(time1=i["showtimes"][j][k])
                # Showtimes.objects.get(movie_identifier=j).initialise_times(Time.objects.get(time=i["showtimes"][j])) # sus on this
            print()

    
    print("name = " + str(Theatres.objects.get(pk=1).showtimes))
            

    movie = Movies.objects.all()
    return render(request, "index.html", {"movie":movie})
        
    
    




    

