# bnb/tests/test_api.py
from django.test import TestCase
from rest_framework.test import APIClient
from bnb.models import Place, User, Country, City, Amenity

class PlaceAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testhost', email='testhost@example.com')
        self.country = Country.objects.create(name='France', code='FR')
        self.city = City.objects.create(name='Paris', country=self.country)
        self.amenity = Amenity.objects.create(name='WiFi')

    def test_create_place(self):
        data = {
            'name': 'New Place',
            'description': 'A lovely place to stay.',
            'city': self.city.id,
            'host': self.user.id,
            'address': '456 Test Avenue',
            'latitude': 48.8566,
            'longitude': 2.3522,
            'number_of_rooms': 2,
            'number_of_bathrooms': 1,
            'price_per_night': 150,
            'max_guests': 4,
            'amenities': [self.amenity.id]
        }
        response = self.client.post('/api/places/', data, format='json')
        self.assertEqual(response.status_code, 201)
