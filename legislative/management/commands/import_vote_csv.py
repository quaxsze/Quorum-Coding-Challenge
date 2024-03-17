import csv
from django.core.management.base import BaseCommand
from legislative.models import Vote


class Command(BaseCommand):
    help = 'Load Vote csv file into the Quorum database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Vote.objects.create(
                    id=int(row['id']),
                    bill_id=int(row['bill_id'])
                )
