from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, World!")

def hai(request):
    return render(request, "index.html", {"message": "hai"})

def loop(request):
    return render(request, "loop.html", {"message": {"first": "first", "second": "second"}})