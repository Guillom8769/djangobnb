import csv
from django.core.management.base import BaseCommand
from bnb.models import Country

class Command(BaseCommand):
    help = 'Load countries from a CSV file into the database'

    def handle(self, *args, **options):
        with open('countries.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row if your CSV has one
            for row in reader:
                country_name = row[0]
                country_code = row[1]  # Assuming your CSV has a second column for the code
                country, created = Country.objects.get_or_create(name=country_name, code=country_code)
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Country '{country.name}' created."))
                else:
                    self.stdout.write(f"Country '{country.name}' already exists.")
