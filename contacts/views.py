from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contacts

def contact(request):
    if request.method== "POST":
        listing_id= request.POST.get('listing_id', False)
        listing=request.POST.get('listing', False)
        name=request.POST.get('name', False)
        email=request.POST.get('email', False)
        phone=request.POST.get('phone', False)
        location=request.POST.get('location', False)
        message=request.POST.get('message', False)
        user_id=request.POST.get('user_id', False)
        realtor_email=request.POST.get('realtor_email', False)

        #check if user has made inquries
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contatacted=Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contatacted:
                messages.error(request, 'You have already made your enquires')
        conatct=Contacts(listing=listing, listing_id=listing_id, name=name, email= email, phone=phone, message=message,user_id= user_id)
        conatct.save()

        send_mail( 'Property Listing Inquiry','Ther has been an inquery on ' + listing + '.Sign into your dashboard panel for more info ', 'obengstoney@gmail.com', [realtor_email, 'obengstoney@gmail.com'], fail_silently=False)
        messages.success(request, 'Your request has been submitted, a realtor will get back to you')
        return redirect('/accounts/dashboard/' )
  
   


        