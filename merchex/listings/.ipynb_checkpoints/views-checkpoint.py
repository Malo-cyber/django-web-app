from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band, Title

def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f'''
    <h1>Hello Django!</h1>
    <ul>
        <li>{bands[0].name}</li>
        <li>{bands[1].name}</li>
        <li>{bands[2].name}</li>
    </ul>
    
    ''')

def about(request):
    return HttpResponse('<h1>About us</h1> <p> On a de grands projet </p>')

def listing(request):
    return HttpResponse('<h1>Listing</h1> <p> ici la liste des ingredient </p>')

def contact(request):
    return HttpResponse('<h1>Contact us</h1> <p> aller viens me faire monter le lait bebe </p>')