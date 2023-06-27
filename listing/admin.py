from django.contrib import admin
from .models import Listing
# from listing.models import Listing

# Register your models here. add here the model or table that you created for the datavase

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'price', 'beds', 'baths', 'sqrt', 'created_at')

admin.site.register(Listing, ListingAdmin)