# bnb/load_countries.py

import csv
import os
import django

# Configurer Django pour qu'il puisse accéder aux modèles
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from bnb.models import Country

def load_countries():
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'countries.csv')
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            Country.objects.get_or_create(code=row['alpha-2'], name=row['name'])

if __name__ == "__main__":
    load_countries()
