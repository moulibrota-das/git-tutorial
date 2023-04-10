from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World Gour Krishna Dey")
def about(request):
    return HttpResponse("About page Gour Krishna")

def contacts(request):
    return HttpResponse("Contacts page")

def services(request):
    return HttpResponse("Services page")