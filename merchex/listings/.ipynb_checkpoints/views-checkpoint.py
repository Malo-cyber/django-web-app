from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Title
from django.shortcuts import render

def hello(request):
    bands = Band.objects.all()
    titles = Title.objects.all()
    return render(request, 
                  'listings/hello.html',
                  {'bands' : bands,
                  'titles' : titles},
                 )


def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    return render(request, 'listings/listing.html')

def contact(request):
    return render(request, 'listings/contact.html')