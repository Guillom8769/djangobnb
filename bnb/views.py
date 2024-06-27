# bnb/views.py
from django.shortcuts import render, get_object_or_404
from .models import User, Place, Review, Amenity, Country, City

def home(request):
    return render(request, 'bnb/home.html')

def place_list(request):
    places = Place.objects.all()
    return render(request, 'bnb/place_list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'bnb/place_detail.html', {'place': place})

def user_list(request):
    users = User.objects.all()
    return render(request, 'bnb/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'bnb/user_detail.html', {'user': user})

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'bnb/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'bnb/review_detail.html', {'review': review})

def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, 'bnb/amenity_list.html', {'amenities': amenities})

def amenity_detail(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    return render(request, 'bnb/amenity_detail.html', {'amenity': amenity})

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'bnb/country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'bnb/country_detail.html', {'country': country})

def city_list(request):
    cities = City.objects.all()
    return render(request, 'bnb/city_list.html', {'cities': cities})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'bnb/city_detail.html', {'city': city})
