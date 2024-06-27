# bnb/views.py
from django.shortcuts import render, get_object_or_404
from .models import Place

def home(request):
    return render(request, 'bnb/home.html')

def place_list(request):
    places = Place.objects.all()
    return render(request, 'bnb/place_list.html', {'places': places})

def place_detail(request, pk):
    place = get_object_or_404(Place, pk=pk)
    return render(request, 'bnb/place_detail.html', {'place': place})
