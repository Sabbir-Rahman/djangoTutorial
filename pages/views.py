from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request,*args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>") #string of html code
    return render(request, "home.html", {})

def contact_view(request,*args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request,*args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123,
        "my_list": [123, 4242, 12313,"ABCD"],
        "check_list": [2,1,3,5,6,8,4,9,11],

    }
    return render(request, "about.html", my_context)