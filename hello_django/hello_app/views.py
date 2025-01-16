from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    anime_for_pass = {
        'animes' : [{
        'title' : 'Onepiece',
        'year' : 1999,
        'sucess' : True,
        'img' : 'onepiece.jpeg'
    },{
        'title' : 'Attack on titan',
        'year' : 2004,
        'summary' : 'Tatakae',
        'sucess' : True,
        'img' : 'eren.jpg'
    },{
        'title' : 'Bleach',
        'year' : 2000,
        'summary' : 'Benkai',
        'sucess' : True,
        'img' : 'bleach.jpeg'
    }]
    }
    return render(request, "hello.html", anime_for_pass)