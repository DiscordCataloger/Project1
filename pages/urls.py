from django.urls import path
from . import views
# set the / api, as variable to callback function
urlpatterns = [
    path('', views.index, name="index"),
    # path('index', views.index, name="index"),
    path('about', views.about, name="about"),
]
