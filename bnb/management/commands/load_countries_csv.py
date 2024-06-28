import csv
from django.core.management.base import BaseCommand
from bnb.models import Country

class Command(BaseCommand):
    help = 'Load countries from a CSV file into the database'

    def handle(self, *args, **options):
        with open('countries.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                country_name = row['name']
                country_code = row['alpha-2']  # Updated to match the CSV header
                country, created = Country.objects.get_or_create(name=country_name, code=country_code)
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Country '{country.name}' created."))
                else:
                    self.stdout.write(f"Country '{country.name}' already exists.")
