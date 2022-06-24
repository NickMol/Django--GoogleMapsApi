import googlemaps
from datetime import datetime
from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *
from django.http import JsonResponse
from django.conf import settings
import requests
import json
import urllib

# Create your views here.

def home(request):
    context = {}
    return render(request, 'google/home.html',context)


def geocode(request):
    clubs = FootballClubs.objects.all()

    context = {
        'clubs':clubs,
    }
    return render(request, 'google/geocode.html',context)

def geocode_club(request,pk):
    club = FootballClubs.objects.get(id=pk)
    # check whether we have the data in the database that we need to calculate the geocode
    if club.adress and club.country and club.zipcode and club.city != None: 
        # creating string of existing location data in database
        adress_string = str(club.adress)+", "+str(club.zipcode)+", "+str(club.city) +", "+str(club.country)
        print(adress_string)

        # geocode the string
        gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
        intermediate = json.dumps(gmaps.geocode(str(adress_string))) 
        intermediate2 = json.loads(intermediate)
        latitude = intermediate2[0]['geometry']['location']['lat']
        longitude = intermediate2[0]['geometry']['location']['lng']
        print(latitude)
        print(longitude)
        # save the lat and long in our database
        club.latitude = latitude
        club.longitude = longitude
        club.save()
        return redirect('geocode')
    else:
        return redirect('geocode')
    return render(request, 'google/empty.html',context)