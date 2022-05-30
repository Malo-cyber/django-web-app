from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Listing
from django.shortcuts import render

def bands_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands_list.html',{'bands' : bands },)

def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    return render(request, 'listings/listing.html')

def contact(request):
    return render(request, 'listings/contact.html')

def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})