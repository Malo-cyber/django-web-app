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
    return HttpResponse('<h1>About us</h1> <p> On a de grands projet </p>')

def listing(request):
    return HttpResponse('<h1>Listing</h1> <p> ici la liste des ingredient </p>')

def contact(request):
    return HttpResponse('<h1>Contact us</h1> <p> aller viens me faire monter le lait bebe </p>')