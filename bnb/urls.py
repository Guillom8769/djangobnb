# bnb/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('places/', views.place_list, name='place_list'),
    path('places/<int:pk>/', views.place_detail, name='place_detail'),
    path('users/', views.user_list, name='user_list'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    path('amenities/', views.amenity_list, name='amenity_list'),
    path('amenities/<int:pk>/', views.amenity_detail, name='amenity_detail'),
    path('countries/', views.country_list, name='country_list'),
    path('countries/<int:pk>/', views.country_detail, name='country_detail'),
    path('cities/', views.city_list, name='city_list'),
    path('cities/<int:pk>/', views.city_detail, name='city_detail'),
]
