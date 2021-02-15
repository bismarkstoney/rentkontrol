from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from listings.models import Listing
from realtors.models import Realtor
from .filters import listingFilters
class HomeListingView(ListView):
    model=Listing
    queryset=Listing.objects.all().order_by('-list_date')
    template_name='pages/index.html'
    paginate_by=3
    context_object_name='listings'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filters"] = listingFilters(self.request.GET, queryset=self.get_queryset())
        return context
    
    



class AboutView(ListView):
    
    model=Realtor
    
    template_name='pages/about.html'
    context_object_name="realtors"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_mvp"] = Realtor.objects.filter(is_pop=True)
        return context
    

