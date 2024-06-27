from django.contrib import admin
from .models import User, Country, City, Amenity, Place, Review

admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Amenity)
admin.site.register(Place)
admin.site.register(Review)
