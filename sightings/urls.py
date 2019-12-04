from django.urls import path

from . import views

app_name='sightings'
urlpatterns = [
        path('',views.index,name="index"),
        path('<unique-squirrel-id>/update/',views.update,name="update"),
        path('add/',views.add,name="add"),
        path('<unique-squirrel-id>/delete/',views.delete,name="delete"),
        path('stats/',views.stats,name="stats"),

]
