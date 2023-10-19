from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# def index(request):
#   return HttpResponse("<h1>Hello</h1>")
# from django.http import HttpResponse
from .models import Listing
from .models import Realtor

'''
def index(request):
    return render(request, 'listings/listings.html', {'name': "something"}) # To render a variable, use a dictionary

OR

def index(request):
    context = {'name': 'something'}
    return render(request, 'listings/listings.html', context) # More frequently used
'''


def index(request):
    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    # GET is a parameter under request module. get (the second get) is a Django parameter. Every time you click on a page, you send a query to the website, to generate a link /listings/?page=x, where ? is query, and page is the variable for the page number loaded.
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    context = {'listings': page_listings}
#   context = {'listings': listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    context = {'listing': listing}
    return render(request, "listings/listing.html", context)


def search(request):
    return render(request, "listings/search.html")
# Create your views here.
