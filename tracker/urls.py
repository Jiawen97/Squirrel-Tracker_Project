from django.urls import path

from . import views

app_name='tracker'
urlpatterns = [
        path('/map',views.map,name='map'),
        path('/sightings',views.list,name='list'),
        path('/sightings/<unique-squirrel-id>',views.update,name='update'),
        path('/sightings/add',views.add,name='add'),
        path('/sightings/<unique-squirrel-id>',views.delete,name='delete'),
        path('/sightings/stats',views.stats,name='stats'),

]
