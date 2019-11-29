from django.shortcuts import render
from .models import sightings
from django.views.generic import ListView

def map(request):
    template_name='traker/map.html'
    model=sightings

class sightings(ListView):
    template_name='list.html'
    def list(request):
        list_all=sightings.objects.all()
        context={'sightings':list_all}
        return render(request,'list.html'context=context)

    def update(request):

    def create(request):

    def delete(request):

    def states(request):
