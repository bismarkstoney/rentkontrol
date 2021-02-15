from django.shortcuts import render
from django.views.generic import DetailView, ListView, DeleteView, CreateView,TemplateView

from .models import Listing
from .filters import listingFilters

class ListingView(ListView):

    
    model=Listing
    paginate_by = 12
    queryset=Listing.objects.all().order_by('list_date')
    context_object_name='listings'
    template_name='listings/listings.html' 
  
    myfilter=listingFilters()


    
     
    
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trending"]=Listing.objects.order_by("list_date")
        context["filters"] = listingFilters(self.request.GET, queryset=self.get_queryset())
        
        return context
    
   


class DetailListingView(DetailView):
    model=Listing
    template_name='listings/listing.html'
    
    


class SearchListing(TemplateView):
    template_name='listings/search.html'