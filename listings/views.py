from django.shortcuts import render
# def index(request):
#   return HttpResponse("<h1>Hello</h1>")
# from django.http import HttpResponse


def index(request):
    return render(request, "listings/listings.html")


def listing(request):
    return render(request, "listings/listing.html")


def search(request):
    return render(request, "listings/search.html")
# Create your views here.
