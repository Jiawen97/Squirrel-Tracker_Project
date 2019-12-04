from django.shortcuts import render,redirect
from .models import sightings
from django.http import HttpResponse

def index(request):
    try:
        sightingss=sightings.objects.all()
        context={
                'sightings':sightingss,
                }
    except Squirrel.NotExist:
        raise Http404("Squirrel does not exist!")
    return render(request,'sightings/index.html',context)

def update(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method=="POST":
        squirrel.longitude=request.POST['longitude']
        squirrel.latitude=request.POST['latitude']
        squirrel.shift=request.POST['shift']
        squirrel.date=request.POST['date']           
        squirrel.age=request.POST['age']
        squirrel.primary_fur_color=request.POST['primary_fur_color']
        squirrel.location=request.POST['location']
        squirrel.specific_location=request.POST['specific_location']
        squirrel.running=request.POST['running']
        squirrel.chasing=request.POST['chasing']
        squirrel.climbing=request.POST['climbing']
        squirrel.eating=request.POST['eating']
        squirrel.foraging=request.POST['foraging']
        squirrel.other_activities=request.POST['other_activities']
        squirrel.kuks=request.POST['kuks']
        squirrel.quaas=request.POST['quaas']
        squirrel.moans=request.POST['moans']
        squirrel.tail_flags=request.POST['tail_flags']
        squirrel.tail_twitches=request.POST['tail_twitches']
        squirrel.approaches=request.POST['approaches']
        squirrel.indifferent=request.POST['indifferent']
        squirrel.runs_from=request.POST['runs_from']
        squirrel.save()
        context={'squirrel':squirrel}
        return render(request,'sightings/details.html',context)
    context={'squirrel':squirrel}
    return render(request,'sightings/update.html',context)

def add(request):
    if request.method=="POST":
        if request.POST.get('latitude') and request.POST.get('longitude') and request.POST.get('Unique_Squirrel_ID'):
            squirrel=sigtings()
            squirrel.longitude=request.POST.get('longitude')
            squirrel.latitude=request.POST.get('latitude')
            squirrel.unique_squirrel_id=request.POST.get('Unique_Squirrel_ID')
            squirrel.shift=request.POST.get('shift')
            squirrel.date=request.POST.get('date')
            squirrel.age=request.POST.get('age')
            squirrel.primary_fur_color=request.POST.get('primary_fur_color')
            squirrel.location=request.POST.get('location')
            squirrel.specific_location=request.POST.get('specific_location')
            squirrel.running=request.POST.get('running')
            squirrel.chasing=request.POST.get('chasing')
            squirrel.climbing=request.POST.get('climbing')
            squirrel.eating=request.POST.get('eating')
            squirrel.foraging=request.POST.get('foraging')
            squirrel.other_activities=request.POST.get('other_activities')
            squirrel.kuks=request.POST.get('kuks')
            squirrel.quaas=request.POST.get('quaas')
            squirrel.moans=request.POST.get('moans')
            squirrel.tail_flags=request.POST.get('tail_flags')
            squirrel.tail_twitches=request.POST.get('tail_twitches')
            squirrel.approaches=request.POST.get('approaches')
            squirrel.indifferent=request.POST.get('indifferent')
            squirrel.runs_from=request.POST.get('runs_from')
            squirrel.save()
            context={'Squirrel':sightings.objects.all()[:50],}
            return render(request,'sightings/index.html',context)
    else:
            return render(request,'sightings/add.html')

def delete(request,Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID) 
    if request.method =="POST":
        squirrel.delete()
        return redirect('sightings:index')
    return render(request,'sightings/delete.html')
    
def stats(request):
    sightings_stats1=Squirrel.objects.all().count()
    sightings_stats2=Squirrel.objects.filter(Primary_fur_color='Black').count()
    sightings_stats3=Squirrel.objects.filter(Primary_fur_color='Gray').count()
    sightings_stats4=Squirrel.objects.filter(Age='Adult').count()
    sightings_stats5=Squirrel.objects.filter(Age='Juvenile').count()
    context={
            'sightings_stats1':sightings_stats1,
            'sightings_stats2':sightings_stats2,
            'sightings_stats3':sightings_stats3,
            'sightings_stats3':sightings_stats3,
            'sightings_stats4':sightings_stats4,
            'sightings_stats5':sightings_stats5,
            }
    return render(request, 'sightings/stats.html', context)
