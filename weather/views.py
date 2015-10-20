from django.shortcuts import render_to_response, RequestContext
from django.core.context_processors import csrf
import urllib2
from json import load
from common.forms import CityForm
from django.conf import settings

# Example API call:
# http://api.openweathermap.org/data/2.5/weather?q=Brooklyn&appid=APIKEYGOESHERE


def get_weather(request):
    app_title = 'Curly or Straight?'

    # process the form data on POST requests
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = CityForm(request.POST)
        if form.is_valid():
            city = str(form.cleaned_data['your_city'])
            app_title = 'Forecast for ' + city

            # Remove whitespace from submissions like 'los angeles'
            city = city.replace(' ', '')

            # Get API key from settings
            owm_key = settings.OWM_API
            url = ('http://api.openweathermap.org/data/2.5/weather?q='
                   + city + '&appid=' + owm_key)

            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            json_obj = load(response)

            # Weather data for template
            humidity = json_obj['main']['humidity']
            general = json_obj['weather'][0]['description']
            wind_speed = json_obj['wind']['speed']
            headline = 'Go curly OR straight!'
            subheadline = 'The weather is pretty in-between, so rock whatever hairstyle you want to.'

            if humidity > 50 and wind_speed > 10:
                headline = 'Wear it straight.'
                subheadline = '''Even though it is humid, the wind will mess up your hair.
                              '''

            elif humidity > 50 and wind_speed < 10:
                headline = 'Wear it curly!'
                subheadline = "It's humid out but not too windy!"

            elif wind_speed > 11:
                headline = 'Wear a ponytail!'
                subheadline = "It's pretty windy today, so wear your hair up!"

            # csrf token update
            c = {}
            c.update(csrf(request))

            context = {'title': app_title,
                       'form': form,
                       'humidity': humidity,
                       'general': general,
                       'wind_speed': wind_speed,
                       'headline': headline,
                       'subheadline': subheadline,
                       }
    else:
        # If loading the page without submitting a form, create a form.
        form = CityForm()
        context = {'title': app_title, 'form': form}

    return render_to_response('weather/weather_home.html',
                              context,
                              context_instance=RequestContext(request))
