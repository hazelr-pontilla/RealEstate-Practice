from django.forms import ModelForm
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'address',
            'price',
            'beds',
            'baths',
            'sqrt',
            'image',
            'description'
        ]
