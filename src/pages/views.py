from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello World!</h1>") # string of HTML code.
    return render(request, "home.html",{})

def contactpage(request, *args, **kwargs):
    return render(request, "contact.html",{})

def about_view(request, *args, **kwargs):
    my_context = {
        "title":"This about us",
        "this_is_true": True,
        "my_list":[123,234,1112, "Abc"],
        "my_html": "<h1> Hello World!</h1>"
    }
    return render(request, "about.html", my_context)

def social_view(request, *args, **kwargs):
    return HttpResponse("<h1> Social page</h1>")