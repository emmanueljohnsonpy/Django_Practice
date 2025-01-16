from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the home page", status=300)  # OK

def create(request):
    return HttpResponse("This is the create page", status=201)  # Created

def edit(request):
    return HttpResponse("This is the edit page", status=200)  # OK

def list(request):
    return HttpResponse("This is the list page", status=200)  # OK

def fstatic(request):
    return HttpResponse("This is the static page", status=200)  # OK
