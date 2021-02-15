
from django.urls import path
from .views import ListingView, DetailListingView,SearchListing


urlpatterns = [
    path('', ListingView.as_view(), name='listings'),
    path('<uuid:slug>/', DetailListingView.as_view(), name='listing'),
    path('search/', SearchListing.as_view(), name='search'),
]