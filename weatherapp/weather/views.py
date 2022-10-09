from django.shortcuts import render
import requests
from.models import City
from. forms import CityForm

def index(request):
    appid = '61839f00d2f6bd4bcd19106733109310'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities=[]
    for city in cities:
        res = requests.get(url.format(city)).json()
        info = {
            'city': city,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]['icon'],
            'humidity': res["main"]['humidity']
        }
        all_cities.append(info)


    context = {'all_info': all_cities, 'form':form}
    return render(request, "weather/index.html", context)
