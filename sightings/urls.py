from django.urls import path

from . import views

app_name='sightings'
urlpatterns = [
        path('',views.index,name="index"),
        path('<Unique_Squirrel_ID>/update/',views.update,name="update"),
        path('add/',views.add,name="add"),
        path('<Unique_Squirrel_ID>/delete/',views.delete,name="delete"),
        path('stats/',views.stats,name="stats"),
        path('<Unique_Squirrel_ID>/details/',views.details,name="details")

]
