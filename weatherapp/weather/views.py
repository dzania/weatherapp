from django.shortcuts import render
import requests
from weather.RequestsManager import RequestsManager
from .TemperatureConverter import TemperatureConverter
from .weatherparser import WeatherParser 
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.
def index(request):
    city = str(request.POST.get('city'))
    submitbutton = request.POST.get('Submit')

    if city == None:
        messages.warning(request,"Please enter city")
    
    get_api = RequestsManager()
    data_from_server = get_api.make_request(city)
    if data_from_server == None:
        messages.error(request,"Oops Entered city not correct please try again!")
        return render(request,'weather/index.html')


    else:
        data = WeatherParser()
        parsed_data = data.get_parsed_weather_data(data_from_server)    
        weather_dict = {
            'city': parsed_data[0],
            'temperature': parsed_data[1],
            'windspeed':parsed_data[2],
            'mintemp':parsed_data[3],
            'maxtemp':parsed_data[4],
            'description':parsed_data[5],
        }
        
        context = {'submitbutton':submitbutton, 'parsed_data': weather_dict}
        return render(request, 'weather/index.html',context)
        
