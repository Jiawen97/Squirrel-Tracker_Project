from django.shortcuts import render,redirect
from .models import sightings
from django.http import HttpResponse
from django.http import Http404

def index(request):
    try:
        Sightings=sightings.objects.all()
        context={
                'sightings':Sightings,
                }
    except:
        raise Http404("Squirrel does not exist!")
    return render(request,'sightings/index.html',context)

def update(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        squirrel.Longitude=request.POST['longitude']
        squirrel.Latitude=request.POST['latitude']
        squirrel.Shift=request.POST['shift']
        squirrel.Date=request.POST['date']           
        squirrel.Age=request.POST['age']
        squirrel.Primary_Fur_Color=request.POST['primary_fur_color']
        squirrel.Location=request.POST['location']
        squirrel.Specific_Location=request.POST['specific_location']
        squirrel.Running=request.POST['running']
        squirrel.Chasing=request.POST['chasing']
        squirrel.Climbing=request.POST['climbing']
        squirrel.Eating=request.POST['eating']
        squirrel.Foraging=request.POST['foraging']
        squirrel.Other_activities=request.POST['other_activities']
        squirrel.Kuks=request.POST['kuks']
        squirrel.Quaas=request.POST['quaas']
        squirrel.Moans=request.POST['moans']
        squirrel.Tail_flags=request.POST['tail_flags']
        squirrel.Tail_twitches=request.POST['tail_twitches']
        squirrel.Approaches=request.POST['approaches']
        squirrel.Indifferent=request.POST['indifferent']
        squirrel.Runs_from=request.POST['runs_from']
        squirrel.save()
        context={'squirrel':squirrel}
        return render(request,'sightings/details.html',context)
    context={'squirrel':squirrel}
    return render(request,'sightings/update.html',context)

def add(request):
    if request.method=="POST":
        if request.POST.get('latitude') and request.POST.get('longitude') and request.POST.get('unique_squirrel_id'):            
            squirrel=sightings()
            squirrel.Longitude=request.POST.get('longitude')
            squirrel.Latitude=request.POST.get('latitude')
            squirrel.Unique_Squirrel_ID=request.POST.get('unique_squirrel_id')
            squirrel.Shift=request.POST.get('shift')
            squirrel.Date=request.POST.get('date')
            squirrel.Age=request.POST.get('age')
            squirrel.Primary_Fur_Color=request.POST.get('primary_fur_color')
            squirrel.Location=request.POST.get('location')
            squirrel.Specific_Location=request.POST.get('specific_location')
            squirrel.Running=request.POST.get('running')
            squirrel.Chasing=request.POST.get('chasing')
            squirrel.Climbing=request.POST.get('climbing')
            squirrel.Cating=request.POST.get('eating')
            squirrel.Foraging=request.POST.get('foraging')
            squirrel.Other_Activities=request.POST.get('other_activities')
            squirrel.Kuks=request.POST.get('kuks')
            squirrel.Quaas=request.POST.get('quaas')
            squirrel.Moans=request.POST.get('moans')
            squirrel.Tail_flags=request.POST.get('tail_flags')
            squirrel.Tail_twitches=request.POST.get('tail_twitches')
            squirrel.Approaches=request.POST.get('approaches')
            squirrel.Indifferent=request.POST.get('indifferent')
            squirrel.Runs_from=request.POST.get('runs_from')
            squirrel.save()
            context={'sightings':sightings.objects.all(),}
            return render(request,'sightings/index.html',context)
    else:
            return render(request,'sightings/add.html')

def delete(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID) 
    if request.method =="POST":
        squirrel.delete()
        return redirect('sightings:index')
    return render(request,'sightings/delete.html')
    
def stats(request):
    sightings_stats1=sightings.objects.all().count()
    sightings_stats2=sightings.objects.filter(Primary_fur_color='Black').count()
    sightings_stats3=sightings.objects.filter(Primary_fur_color='Gray').count()
    sightings_stats4=sightings.objects.filter(Age='Adult').count()
    sightings_stats5=sightings.objects.filter(Age='Juvenile').count()
    context={
            'sightings_stats1':sightings_stats1,
            'sightings_stats2':sightings_stats2,
            'sightings_stats3':sightings_stats3,
            'sightings_stats3':sightings_stats3,
            'sightings_stats4':sightings_stats4,
            'sightings_stats5':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)

def details(request,Unique_Squirrel_ID):
    squirrel = sightings.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    context = {'squirrel':squirrel,}
    return render(request,'sightings/details.html',context)
