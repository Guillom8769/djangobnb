from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Place, Review, Amenity, Country, City
from .forms import UserForm, PlaceForm, ReviewForm, AmenityForm, CountryForm, CityForm

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

# User CRUD views
def user_list(request):
    users = User.objects.all()
    return render(request, 'bnb/user_list.html', {'users': users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'bnb/user_detail.html', {'user': user})

def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'bnb/user_form.html', {'form': form})

def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', pk=user.pk)
    else:
        form = UserForm(instance=user)
    return render(request, 'bnb/user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'bnb/user_confirm_delete.html', {'user': user})

# Place CRUD views
def place_list(request):
    places = Place.objects.all()
    return render(request, 'bnb/place_list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'bnb/place_detail.html', {'place': place})

def place_create(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('place_list')
    else:
        form = PlaceForm()
    return render(request, 'bnb/place_form.html', {'form': form})

def place_update(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        form = PlaceForm(request.POST, instance=place)
        if form.is_valid():
            form.save()
            return redirect('place_detail', pk=place.pk)
    else:
        form = PlaceForm(instance=place)
    return render(request, 'bnb/place_form.html', {'form': form})

def place_delete(request, pk):
    place = get_object_or_404(Place, pk=pk)
    if request.method == "POST":
        place.delete()
        return redirect('place_list')
    return render(request, 'bnb/place_confirm_delete.html', {'place': place})

# Similar views for Review, Amenity, Country, City...
def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'bnb/review_list.html', {'reviews': reviews})

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'bnb/review_detail.html', {'review': review})

def review_create(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'bnb/review_form.html', {'form': form})

def review_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=review.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'bnb/review_form.html', {'form': form})

def review_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect('review_list')
    return render(request, 'bnb/review_confirm_delete.html', {'review': review})

def amenity_list(request):
    amenities = Amenity.objects.all()
    return render(request, 'bnb/amenity_list.html', {'amenities': amenities})

def amenity_detail(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    return render(request, 'bnb/amenity_detail.html', {'amenity': amenity})

def amenity_create(request):
    if request.method == "POST":
        form = AmenityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('amenity_list')
    else:
        form = AmenityForm()
    return render(request, 'bnb/amenity_form.html', {'form': form})

def amenity_update(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == "POST":
        form = AmenityForm(request.POST, instance=amenity)
        if form.is_valid():
            form.save()
            return redirect('amenity_detail', pk=amenity.pk)
    else:
        form = AmenityForm(instance=amenity)
    return render(request, 'bnb/amenity_form.html', {'form': form})

def amenity_delete(request, pk):
    amenity = get_object_or_404(Amenity, pk=pk)
    if request.method == "POST":
        amenity.delete()
        return redirect('amenity_list')
    return render(request, 'bnb/amenity_confirm_delete.html', {'amenity': amenity})

def country_list(request):
    countries = Country.objects.all()
    return render(request, 'bnb/country_list.html', {'countries': countries})

def country_detail(request, pk):
    country = get_object_or_404(Country, pk=pk)
    return render(request, 'bnb/country_detail.html', {'country': country})

def country_create(request):
    if request.method == "POST":
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('country_list')
    else:
        form = CountryForm()
    return render(request, 'bnb/country_form.html', {'form': form})

def country_update(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        form = CountryForm(request.POST, instance=country)
        if form.is_valid():
            form.save()
            return redirect('country_detail', pk=country.pk)
    else:
        form = CountryForm(instance=country)
    return render(request, 'bnb/country_form.html', {'form': form})

def country_delete(request, pk):
    country = get_object_or_404(Country, pk=pk)
    if request.method == "POST":
        country.delete()
        return redirect('country_list')
    return render(request, 'bnb/country_confirm_delete.html', {'country': country})

def city_list(request):
    cities = City.objects.all()
    return render(request, 'bnb/city_list.html', {'cities': cities})

def city_detail(request, pk):
    city = get_object_or_404(City, pk=pk)
    return render(request, 'bnb/city_detail.html', {'city': city})

def city_create(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('city_list')
    else:
        form = CityForm()
    return render(request, 'bnb/city_form.html', {'form': form})

def city_update(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('city_detail', pk=city.pk)
    else:
        form = CityForm(instance=city)
    return render(request, 'bnb/city_form.html', {'form': form})

def city_delete(request, pk):
    city = get_object_or_404(City, pk=pk)
    if request.method == "POST":
        city.delete()
        return redirect('city_list')
    return render(request, 'bnb/city_confirm_delete.html', {'city': city})
