# bnb/forms.py
from django import forms
from .models import User, Place, Review, Amenity, Country, City

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ['name', 'description', 'address', 'city', 'latitude', 'longitude', 'host', 'number_of_rooms', 'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenities']
        widgets = {
            'city': forms.Select()
        }

        country = forms.ModelChoiceField(queryset=Country.objects.all(), to_field_name="name")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'place', 'rating', 'comment']

class AmenityForm(forms.ModelForm):
    class Meta:
        model = Amenity
        fields = ['name']

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'code']

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'country']
        widgets = {
            'country': forms.Select()
        }
