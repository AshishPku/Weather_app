from django.shortcuts import render

# Create your views here.
import urllib.request
import json
def home(request):
    if request.method == 'POST':
        
        city = request.POST['city']
        source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='
                                + city + '&units=metric&appid=cebe49ef10e4832e338c1c5c9d8c299a').read()
        list_of_data=json.loads(source)
        data={
            "country_code" : str(list_of_data['sys']['country']),
            "coordinate" : str(list_of_data['coord']['lon']) + ',' + str(list_of_data['coord']['lat']),
            "temp" : str(list_of_data['main']['temp']),
            "pressure" : str(list_of_data['main']['pressure']),
            "humidity" : str(list_of_data['main']['humidity']),
            "main" : str(list_of_data['weather'][0]['main']),
            "description" : str(list_of_data['weather'][0]['description']),
            "icon" : list_of_data['weather'][0]['icon'],
            "speed" : list_of_data['wind']['speed'],
            "name" : list_of_data['name'],
        }
    else:
        data = {}
    return render(request,"home.html",data)
def about(request):
    return render(request,'about.html')