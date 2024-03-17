import csv
from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from legislative.models import Bill, Legislator


class Command(BaseCommand):
    help = 'Load a csv file into the Bill database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file_path', type=str, help='The CSV file path')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file_path']
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                primary_sponsor_id = int(row['sponsor_id'])
                try:
                    primary_sponsor = Legislator.objects.get(pk=primary_sponsor_id)
                except ObjectDoesNotExist:
                    print(f"Legislator with ID {primary_sponsor_id} does not exist. Import aborted.")
                    return

                Bill.objects.create(
                    id=row['id'],
                    title=row['title'],
                    primary_sponsor=primary_sponsor
                )
        print("Bills import completed successfully.")
