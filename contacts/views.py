from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages, auth
from django.core.mail import send_mail


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST["realtor_email"]
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this listing!")
                return redirect('/listings/'+listing_id)
            contact = Contact(listing=listing, listing_id=listing_id, name=name,
                              email=email, phone=phone, message=message, user_id=user_id)
            contact.save()
            send_mail(
                'Listing Inquiry',
                'Inquiry for ' + listing +
                '. Sign into admin for more info', 'cat2006house@yahoo.com.hk', [
                    realtor_email, 'cat2006house@yahoo.com.hk'],
                fail_silently=False
            )
            messages.success(
                request, 'Your request is submitted. A realtor will get back to you soon!')
            return redirect('/listings/'+listing_id)

# Create your views here.
