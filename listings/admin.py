from django.contrib import admin
from .models import Listing
@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display=('id', 'title', 'is_published', 'price', 'list_date', 'realtor', 'selfmeter')
    list_display_links=('id', 'title')
    list_filter=('realtor', )
    search_fields=('title', 'description', 'address', 'city')
    list_per_page=25

    



