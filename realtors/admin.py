from django.contrib import admin
from .models import Realtor

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
    list_display=('id', 'name', 'email', 'join_date')
    list_display_links=('id', 'name')
    list_filter=('name',)
    list_per_page=25
    


