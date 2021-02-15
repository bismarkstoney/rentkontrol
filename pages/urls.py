from django.urls import path, re_path
from . views import  HomeListingView, AboutView



urlpatterns = [
       path('', HomeListingView.as_view(), name='index'),
       path('about/',AboutView.as_view() , name='about')
]