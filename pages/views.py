from django.shortcuts import render
# def index(request):
 #   return HttpResponse("<h1>Hello</h1>")
# from django.http import HttpResponse
def index(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")
# Create your views here.
