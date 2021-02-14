from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, CreateView,TemplateView

from .models import Listing


class ListingView(ListView):
    model=Listing
    paginate_by = 12
    queryset=Listing.objects.all()
    context_object_name='listings'

    template_name='listings/listings.html' 
  
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        
        context["trending"]=Listing.objects.order_by("list_date")
       
        return context
    
   


class DetailListingView(TemplateView):
    template_name='listings/listing.html'


class SearchListing(TemplateView):
    template_name='listings/search.html'