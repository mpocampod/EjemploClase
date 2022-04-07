from email.mime import image
from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie

def home (request): 
    searchTerm= request.GET.get('searchMovie')
    
    movies=Movie.objects.filter(title=searchTerm)

    return render (request, 'home.html' , {'searchTerm': searchTerm, 'movies': movies})

def about (request):
    return HttpResponse('<h1> Welcome to About Page </h1>')

# Create your views here.
