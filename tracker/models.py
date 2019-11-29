from django.db import models

Class sightings(models.Model):
    Latitude=models.DecimalField( help_text=_('Longitude'),)
    
    Longitude=models.DecimalField(help_text=_('Latitude'),)
    
    Unique_Squirrel_ID=models.CharField(max_length=100, help_text=_('ID of squirrel'),)

    PM='PM'
    AM='AM'
    SHIFT_choices=(
            (PM,'PM'),
            (AM,'AM'),)
    Shift = models.CharField(max_length=2,choices=SHIFT_choices,))
    
    Date=models.DateField(help_text=_('Date'),)

    Age=models.IntegerField(help_text=_('Age'),)
    
    Gray='Gray'
    Cinnamon='Cinnamon'
    Black='Black'
    Other='Other'
    Primary_Fur_Color_choices=( (Gray,'Gray'), (Cinnamon,'Cinnamon'),
    (Black,'Black'),    (Other,'Other'))

    Primary_Fur_Color=models.CharField(max_length=100,choices=Primary_Fur_Color_choices,default=other)

    Ground_Plane='Ground_Plane'
    Above_Ground='Above_Ground'
    Other='Other'
    Location_choices=( (Ground_Plane,'Ground_Plane'), (Above_Ground,'Above_Ground'), (Other,'Other'))
   
    Location=models.CharField(max_length=100,choices=Location_choices)

    Specific_Location=models.CharField(max_length=100)
    
    Running=models.BooleanField(default=False)
    
    Chasing=models.BooleanField(default=False)
    
    Climbing=models.BooleanField(default=False)
    
    Eating=models.BooleanField(default=False)
    
    Foraging=models.BooleanField(default=False)
    
    Other_Activities=models.CharField(max_length=100)
    
    Kuks=models.BooleanField(default=False)
    
    Quaas=models.BooleanField(default=False)
    
    Moans=models.BooleanField(default=False)
    
    Tail_flags=models.BooleanField(default=False)
    
    Tail_twitches=models.BooleanField(default=False)
    
    Approaches=models.BooleanField(default=False)
    
    Indifferent=models.BooleanField(default=False)
    
    Runs_from=models.BooleanField(default=False)

