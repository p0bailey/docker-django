from django.shortcuts import render
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Rango says hey there world!")

def index(request):


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'home/index.html')
