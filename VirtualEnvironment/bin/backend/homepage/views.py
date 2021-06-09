import json

from django.shortcuts import *
from .models import Movies, Time, Theatres
from django.http import JsonResponse, HttpResponse


# Create your views here.
path_movies = '/Users/zara/Arludo/VirtualEnvironment/bin/backend/vue_app/movie-app/src/movie_metadata.json'
path_showtimes = '/Users/zara/Arludo/VirtualEnvironment/bin/backend/vue_app/movie-app/src/theater_showtimes.json'
 
def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data

def read_json(path):
    return json.loads(read_file(path))

def get_movies(request):
    var = read_json(path_movies)
    print(var)
    return JsonResponse({"movies": read_json(path_movies)})


def index(request):
    print("Amount of movies: " + str(Movies.objects.count()))
    if Movies.objects.count() == 0:
        all_movies = read_json(path_movies)
        for i in all_movies:
            Movies.objects.create(identifier=i["id"], title=i["title"], rating=i["rating"], poster=i["poster"])
 

        all_theaters = read_json(path_showtimes)
        for i in all_theaters:
            # print("id  =       " + str(i["id"]))
            # print("name =      " + str(i["name"]))
            # print("showtimes = ")
            Theatres.objects.create(identifier = i["id"], name=i["name"])
            for j in i["showtimes"]:
                # print("movie ID: " + str(j))
                # print("time: ")
                        
                for k in range(len(i["showtimes"][j])):
                    # print(i["showtimes"][j][k])
                    Time.objects.create(time=i["showtimes"][j][k], movieID=j, theatreID=i["id"])
                
                # print()

    movie = Movies.objects.all()
    theatres = Theatres.objects.all()
    times = Time.objects.all()
    for time in times:
        print(time.time)
        print(time.movieID)
        print(movie.get(identifier=time.movieID))
        # time.movie.add(movie.get(identifier=time.movieID))
        print(time.theatreID)
        print(theatres.get(identifier=time.theatreID))
        print()



    return render(request, "index.html", {"movie":movie, "theatres": theatres, "times": times})

def get_matching_titles(request, user_title):
    matching_movies = Movies.objects.filer(title= user_title)
    return render(request, "index.html", {"movie":matching_movies})
        
    
    




    

