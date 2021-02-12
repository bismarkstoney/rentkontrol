from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, CreateView,TemplateView


class ListingView(TemplateView):
    template_name='listings/listings.html'


class DetailListingView(TemplateView):
    template_name='listings/listing.html'


class SearchListing(TemplateView):
    template_name='listings/search.html'