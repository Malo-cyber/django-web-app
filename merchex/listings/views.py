from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect

from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandAddForm
from django.shortcuts import render
from django.core.mail import send_mail

def bands_list(request):
    bands = Band.objects.all()
    return render(request, 'listings/bands_list.html',{'bands' : bands },)

def about(request):
    return render(request, 'listings/about.html')

def listing(request):
    return render(request, 'listings/listing.html')

def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz','m.couvet@icloud.com'],)

        return redirect('email-sent') 
    else:
        form = ContactUsForm()

    return render(request, 'listings/contact.html',{'form' : form})

def bands_add(request):
    if request.method == 'POST':
        form = BandAddForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)

    else:
        form = BandAddForm()
    return render(request, 'listings/bands_add.html', {'form' : form})

def band_change(request, id):
    band = Band.objects.get(id=id)
    if request.method =='POST':
        form = BandAddForm(request.POST, instance = band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandAddForm(instance = band)
    
    return render(request, 'listings/band_change.html',{'form' : form})

def email_sent(request):
    return render(request, 'listings/email_sent.html')

def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)
    return render(request, 'listings/band_detail.html', {'band': band})

def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        return redirect('bands-list')
    return render(request, 'listings/band_delete.html', {'band' : band})