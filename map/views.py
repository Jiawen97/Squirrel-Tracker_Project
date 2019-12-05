from django.shortcuts import render
from sightings.models import sightings
def index(request): 
    list_all=sightings.objects.all() 
    context = {'list_all':list_all,} 
    return render(request,'map/index.html',context)
