from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>") #string of html code

def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact page</h1>") #string of html code