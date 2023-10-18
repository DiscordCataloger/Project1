from django.shortcuts import render
# def index(request):
#   return HttpResponse("<h1>Hello</h1>")
# from django.http import HttpResponse
from .models import Listing

'''
def index(request):
    return render(request, 'listings/listings.html', {'name': "something"}) # To render a variable, use a dictionary

OR

def index(request):
    context = {'name': 'something'}
    return render(request, 'listings/listings.html', context) # More frequently used
'''


def index(request):
    listings = Listing.objects.all()
    context = {'listings': listings}
    return render(request, 'listings/listings.html', context)


def listing(request):
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")
# Create your views here.
