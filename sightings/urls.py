from django.urls import path

from . import views

app_name='sightings'
urlpatterns = [
        path('',views.index),
        path('<unique-squirrel-id>/',views.update),
        path('add/',views.add),
        path('<unique-squirrel-id>/',views.delete),
        path('stats/',views.stats),

]
