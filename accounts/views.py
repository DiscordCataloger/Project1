from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from listings.models import Listing


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:  # check address and see if it is not unique address of None
            auth.login(request, user)
            # messages.success(request, "You are now logging in!")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

        # print("login")
        # return redirect("login")
    else:
        return render(request, 'accounts/login.html')


def register(request):

    if request.method == "POST":
        first_name = request.POST['first_name']  # variable in register.html
        last_name = request.POST['last_name']  # variable in register.html
        username = request.POST['username']  # variable in register.html
        email = request.POST['email']  # variable in register.html
        password = request.POST['password']  # variable in register.html
        password2 = request.POST['password2']  # variable in register.html

        if password == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, "Username existed!")
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=username, password=password, email=email,
                    first_name=first_name, last_name=last_name)
                user.save()
                messages.success(request, "You are now registered!")
                return redirect('login')

        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    listings = Listing.objects.all().order_by(
        'id').filter(is_published=True)
    context = {
        'listings': listings,
    }
    return render(request, 'accounts/dashboard.html', context)

# Create your views here.
