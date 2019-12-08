from django.core.management.base import BaseCommand, CommandError
from sightings.models import sightings
import csv
import datetime

class Command(BaseCommand):
    help ='Import Sightings Data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('path', help='/path/to/file.csv',type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, mode='r') as fp:
            reader = csv.DictReader(fp)
            data = list(reader)           
            
            id_bulk=[]
            sightingss=[]
            for row in data:
                if row.get('Unique Squirrel ID') in id_bulk:
                    continue
                else:
                    item = sightings(
                    Longitude = row.get('X'),
                    Latitude = row.get('Y'),
                    Unique_Squirrel_ID = row.get('Unique Squirrel ID'),
                    Shift = row.get('Shift'),
                    Date = datetime.date(int(row.get('Date')[-4:]),int(row.get('Date')[:2]),int(row.get('Date')[2:4])),
                    Age = row.get('Age'),
                    Primary_Fur_Color = row.get('Primary Fur Color'),
                    Location = row.get('Location'),
                    Specific_Location = row.get('Specific Location'),
                    Running = True if row.get('Running').lower()=='true' else False,
                    Chasing = True if row.get('Chasing').lower()=='true' else False,
                    Climbing = True if row.get('Climbing').lower()=='true' else False,
                    Eating = True if row.get('Eating').lower()=='true' else False,
                    Foraging = True if row.get('Foraging').lower()=='true' else False,
                    Other_Activities = row.get('Other Activities'),
                    Kuks = True if row.get('Kuks').lower()=='true' else False,
                    Quaas = True if row.get('Quaas').lower()=='true' else False,
                    Moans = True if row.get('Moans').lower()=='true' else False,
                    Tail_flags = True if row.get('Tail flags').lower()=='true' else False,
                    Tail_twitches = True if row.get('Tail twitches').lower()=='true' else False,
                    Approaches = True if row.get('Approaches').lower()=='true' else False,
                    Indifferent = True if row.get('Indifferent').lower()=='true' else False,
                    Runs_from = True if row.get('Runs from').lower()=='true' else False
                    )
                    sightingss.append(item)
                    id_bulk.append(row.get('Unique Squirrel ID'))
            sightings.objects.bulk_create(sightingss)
            self.stdout.write(self.style.SUCCESS('Import Done'))

                    
