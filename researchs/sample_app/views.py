from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def print_hello(request):
    movie_details={
    'movies':[{
        'title' : 'One Piece',
        'year' : 1999,
        'summary' : 'Gum Gum Pistol',
        'sucess' : True
    },{
        'title' : 'Attack on Titan',
        'year' : 2004,
        'summary' : 'Tatakae',
        'sucess' : True
    },{
        'title' : 'Bleach',
        
        'summary' : 'Benkai',
        'sucess' : True
    }]
    }
    return render(request,'index.html',movie_details)