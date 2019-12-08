from django.core.management.base import BaseCommand, CommandError
from sightings.models import sightings
from django.apps import apps
import csv

class Command(BaseCommand):

    help = 'Exports sightings data to CSV file'

    def add_arguments(self, parser):
        parser.add_argument('path', help='/path/to/file.csv', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'w', newline='') as fp:

            attributes = ['Latitude', 
            			'Longitude', 
            			'Unique_Squirrel_ID', 
            			'Shift', 
            			'Date', 
            			'Age', 
            			'Primary_Fur_Color', 
            			'Location',
                        'Specific_Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_flags',
                        'Tail_twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_from']

            writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)

            for row in sightings.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])

        self.stdout.write(self.style.SUCCESS('Export Done'))




