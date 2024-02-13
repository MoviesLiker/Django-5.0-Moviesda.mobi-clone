from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def home(request):
    category = Category.objects.all().values()
    data = {
        'category': category
    }
    return render(request, 'home.html', data)


def list(request, id):
    category = Category.objects.filter(id=id).values()[0]
    movies = Movie.objects.filter(category=id).values()
    data = {
        'category': category,
        'movies': movies
    }
    return render(request, 'list.html', data)


def movie(request, id):
    movie = Movie.objects.filter(id=id).values()[0]
    data = {
        'movie': movie
    }
    return render(request, 'movie.html', data)


def video(request, id):
    movie = Movie.objects.filter(id=id).values()[0]
    videos = Video.objects.filter(movie=id).values()
    data = {
        'movie': movie,
        'videos': videos
    }
    return render(request, 'video.html', data)


def download(request, id):
    video = Video.objects.filter(id=id).values()[0]
    data = {
        'video': video
    }
    return render(request, 'download.html', data)
