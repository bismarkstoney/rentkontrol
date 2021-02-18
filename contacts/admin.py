from django.contrib import admin

from .models import Contacts

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'listing', 'email', 'contact_date', 'phone')
    list_display_links=('id', 'name')
    search_fields=('email', 'name', 'listing')
    

        
    

