from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# def index(request):
#   return HttpResponse("<h1>Hello</h1>")
# from django.http import HttpResponse
from .models import Listing
from .models import Realtor
from django.http import Http404
from listings.choices import district_choices, price_choices, bedroom_choices

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
 #   listing = Listing.objects.get(id=listing_id)
    try:
        listing = get_object_or_404(Listing, pk=listing_id)
        context = {'listing': listing,
                   'district': district_choices[listing.district]}
        return render(request, "listings/listing.html", context)
    except Http404:
        return render(request, '404.html')


def search(request):

    queryset_list = Listing.objects.all().order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords
            )

    if 'address' in request.GET:
        address = request.GET['address']
        if address:
            queryset_list = queryset_list.filter(
                address__icontains=address  # contains keywords
            )

    if 'district' in request.GET:
        district = request.GET['district']
        if district:
            district = district_choices[district]
            queryset_list = queryset_list.filter(
                district__iexact=district  # exact district
            )

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms  # less than & equal to
            )

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price  # less than & equal to
            )

    context = {
        'listings': queryset_list,
        'district_choices': district_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'values': request.GET  # Keep the search values and variables in search.html after search
    }
    return render(request, "listings/search.html", context)
# Create your views here.
