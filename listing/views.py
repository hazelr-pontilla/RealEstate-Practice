from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# CRUD = create, retrieve, update, delete, display_list of listings

# Create your views here.
def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings.html', {'listings': listings})

def create(request):
    form = ListingForm()

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create.html', {'form': form})

def retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    return render(request, 'retrieve.html', {'listing': listing})

def update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form,
        'listing': listing
    }
    return render(request, 'update.html', context)

    
def delete(request,pk):
    listing = Listing.objects.get(id=pk)
    listing.delete()
    return redirect('/')