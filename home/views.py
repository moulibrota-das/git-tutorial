from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("New Hello world")

def about(request):
    return HttpResponse("About page")

def contacts(request):
    return HttpResponse("Contacts page")

def services(request):
    return HttpResponse("Services page")
