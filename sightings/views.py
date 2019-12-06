from django.shortcuts import render,redirect,get_object_or_404
from .models import sightings
from django.http import HttpResponse
from django.http import Http404

from .forms import sightingsform

def index(request):
    try:
        Sightings=sightings.objects.all()
        context={
                'sightings':Sightings,
                }
    except:
        raise Http404("Squirrel does not exist!")
    return render(request,'sightings/index.html',context)


def add(request):
    if request.method == "POST":
        form = sightingsform(request.POST)
        if form.is_valid():
            form.save()
            context={'sightings':sightings.objects.all(),}
            return render(request,'sightings/index.html',context)
    else:
        form = sightingsform()
    context = {'form':form}
    return render(request, 'sightings/update.html',context)

def details(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)

def stats(request):
    sightings_stats1=sightings.objects.all().count()
    sightings_stats2=sightings.objects.filter(Primary_Fur_Color='Black').count()
    sightings_stats3=sightings.objects.filter(Running='True').count()
    sightings_stats4=sightings.objects.filter(Age='Adult').count()
    sightings_stats5=sightings.objects.filter(Age='Juvenile').count()
    context={
            'Number of all the sightings':sightings_stats1,
            'Number of black primary fur color sightings':sightings_stats2,
            'Number of running sightings':sightings_stats3,
            'Number of adult sightings':sightings_stats4,
            'Number of juvenile sightings':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)

def update(request,Unique_Squirrel_ID):
    Sightings = get_object_or_404(sightings, Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method == "POST":
        form = sightingsform(request.POST, instance=Sightings)
        if form.is_valid():
            form.save()
            context={'sightings':sightings.objects.all(),}
            return render(request,'sightings/index.html',context)
    else:
        form = sightingsform(instance=Sightings)
    context = {'form':form}
    return render(request, 'sightings/update.html',context)
