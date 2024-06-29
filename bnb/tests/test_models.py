# bnb/tests/test_models.py

from django.test import TestCase
from bnb.models import Place, User, Country, City

class PlaceModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testhost', email='testhost@example.com')
        self.country = Country.objects.create(name='France', code='FR')
        self.city = City.objects.create(name='Paris', country=self.country)
        self.place = Place.objects.create(
            name='Test Place',
            city=self.city,
            host=self.user,
            address='123 Test Street',
            latitude=48.8566,
            longitude=2.3522,
            number_of_rooms=1,
            number_of_bathrooms=1,
            price_per_night=100,
            max_guests=2
        )

    def test_place_creation(self):
        self.assertEqual(self.place.name, 'Test Place')
        self.assertEqual(self.place.city.name, 'Paris')
        self.assertEqual(self.place.host.username, 'testhost')
        self.assertEqual(self.place.address, '123 Test Street')

    def test_place_deletion(self):
        self.place.delete()
        self.assertFalse(Place.objects.filter(id=self.place.id).exists())

    def test_place_update(self):
        self.place.name = 'Updated Place'
        self.place.save()
        self.assertEqual(self.place.name, 'Updated Place')
