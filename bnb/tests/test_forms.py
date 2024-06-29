# bnb/tests/test_forms.py
from django.test import TestCase
from bnb.forms import PlaceForm
from bnb.models import User, Country, City, Amenity

class PlaceFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testhost', email='testhost@example.com')
        self.country = Country.objects.create(name='France', code='FR')
        self.city = City.objects.create(name='Paris', country=self.country)
        self.amenity = Amenity.objects.create(name='WiFi')

    def test_valid_form(self):
        data = {
            'name': 'Test Place',
            'description': 'A nice place to stay.',
            'city': self.city.id,
            'host': self.user.id,
            'address': '123 Test Street',
            'latitude': 48.8566,
            'longitude': 2.3522,
            'number_of_rooms': 1,
            'number_of_bathrooms': 1,
            'price_per_night': 100,
            'max_guests': 2,
            'amenities': [self.amenity.id]
        }
        form = PlaceForm(data=data)
        self.assertTrue(form.is_valid(), form.errors)
