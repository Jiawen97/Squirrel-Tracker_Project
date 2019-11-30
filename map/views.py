from django.shortcuts import render
from .models import sightings

def index(request):
    longitude = [Longitude for Longitude in sightings.objects.all()]
    latitude = [Latitude for Latitude in sightings.objects.all()]
    context = {longitude, latitude,}
    return render(request,'map/index.html',context)
