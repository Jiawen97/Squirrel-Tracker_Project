from django.forms import ModelForm
from .models import sightings

class sightingsform(ModelForm):
    class Meta:
        model=sightings
        fields='__all__'
