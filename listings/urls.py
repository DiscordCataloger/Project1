from django.urls import path
from . import views
# set the / api, as variable to callback function
urlpatterns = [
    path('', views.index, name="listings"),
    path('listing', views.listing, name="listing"),
    path('search', views.search, name="search"),
]
