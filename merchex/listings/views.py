
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listing

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings/hello.html', {'bands':bands})

def about(request):
    return HttpResponse('<h1>A propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing.html', {'listing':listings})

def contact(request):
    return HttpResponse('<h1>Contact!</h1>')