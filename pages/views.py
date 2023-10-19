from django.shortcuts import render
# def index(request):
#   return HttpResponse("<h1>Hello</h1>")
# from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor


def index(request):
    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {'listings': listings}
    return render(request, "pages/index.html", context)


def about(request):
    listings = Listing.objects.all().order_by()
    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True).order_by('hire_date')
    context = {
        'listings': listings,
        'realtors': realtors,
        'mvp_realtor': mvp_realtors
    }
    return render(request, "pages/about.html", context)
# Create your views here.
