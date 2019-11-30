from django.shortcuts import render
from .models import sightings
from django.http import HttpResponse

def index(request):
    sightingss=sightings.objects.all()
    context={
            'sightings':sightingss,
            }
    return render(request,'sightings/index.html',context)

def update(request,Unique_Squirrel_ID):
        return HttpResponse('Hi')
def add(request):
        return HttpResponse('Hi')
def delete(request,Unique_Squirrel_ID):
        return HttpResponse('Hi')
def stats(request):
        return HttpResponse('Hi')
