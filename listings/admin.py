from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_per_page = 25 # No of records per page 
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor','price',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
admin.site.register(Listing, ListingAdmin)
# Register your models here.
