# bnb/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user_list, name='user_list'),
    path('users/new/', views.user_create, name='user_create'),
    path('users/<int:pk>/', views.user_detail, name='user_detail'),
    path('users/<int:pk>/edit/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('places/', views.place_list, name='place_list'),
    path('places/new/', views.place_create, name='place_create'),
    path('places/<int:pk>/', views.place_detail, name='place_detail'),
    path('places/<int:pk>/edit/', views.place_update, name='place_update'),
    path('places/<int:pk>/delete/', views.place_delete, name='place_delete'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/new/', views.review_create, name='review_create'),
    path('reviews/<int:pk>/', views.review_detail, name='review_detail'),
    path('reviews/<int:pk>/edit/', views.review_update, name='review_update'),
    path('reviews/<int:pk>/delete/', views.review_delete, name='review_delete'),
    path('amenities/', views.amenity_list, name='amenity_list'),
    path('amenities/new/', views.amenity_create, name='amenity_create'),
    path('amenities/<int:pk>/', views.amenity_detail, name='amenity_detail'),
    path('amenities/<int:pk>/edit/', views.amenity_update, name='amenity_update'),
    path('amenities/<int:pk>/delete/', views.amenity_delete, name='amenity_delete'),
    path('countries/', views.country_list, name='country_list'),
    path('countries/new/', views.country_create, name='country_create'),
    path('countries/<int:pk>/', views.country_detail, name='country_detail'),
    path('countries/<int:pk>/edit/', views.country_update, name='country_update'),
    path('countries/<int:pk>/delete/', views.country_delete, name='country_delete'),
    path('cities/', views.city_list, name='city_list'),
    path('cities/new/', views.city_create, name='city_create'),
    path('cities/<int:pk>/', views.city_detail, name='city_detail'),
    path('cities/<int:pk>/edit/', views.city_update, name='city_update'),
    path('cities/<int:pk>/delete/', views.city_delete, name='city_delete'),
    # Ajoutez des chemins pour les autres modèles de manière similaire
]
