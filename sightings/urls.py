from django.urls import path

from . import views

app_name='sightings'
urlpatterns = [
        path('',views.index,name="index"),
        path('add/',views.add,name="add"),
        path('stats/',views.stats,name="stats"),
        path('<Unique_Squirrel_ID>/details/',views.details,name="details"),
        path('<Unique_Squirrel_ID>/',views.update, name="update"),

        ]
