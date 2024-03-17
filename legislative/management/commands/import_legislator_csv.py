import csv
from django.core.management.base import BaseCommand
from legislative.models import Legislator


class Command(BaseCommand):
    help = 'Load legislator csv file into the Quorum database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Legislator.objects.create(
                    id=int(row['id']),
                    name=row['name'],
                )
        print("Legislators import completed successfully.")
