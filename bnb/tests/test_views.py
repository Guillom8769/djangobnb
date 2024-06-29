# bnb/tests/test_views.py
from django.test import TestCase
from django.urls import reverse
from bnb.models import Place, User, Country, City

class PlaceViewTests(TestCase):
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

    def test_place_list_view(self):
        response = self.client.get(reverse('place_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Place')

    def test_place_detail_view(self):
        response = self.client.get(reverse('place_detail', args=[self.place.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Place')
