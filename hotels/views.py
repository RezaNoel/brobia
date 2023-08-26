from django.shortcuts import render
from main.models import City,Hotel
# Create your views here.

def list(request, city_slug):
    city = City.objects.get(slug=city_slug)
    cities = City.objects.all()
    hotels_count = Hotel.objects.filter(city=city.id).count()
    hotels = Hotel.objects.filter(city=city.id)

    content = {"city": city,
               "cities": cities,
               "hotels": hotels,
               "hotel_count": hotels_count}

    return render(request, 'hotels/hotel-list.html', content)