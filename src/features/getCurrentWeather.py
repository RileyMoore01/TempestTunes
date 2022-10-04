# import required modules
import requests, json
from pickletools import long1
from models import CurrentWeather

#Global variables
OPEN_WEATHER_MAP_APIKEY = 'fed200574f31448d3c4ef74409fc60bf'
ZIP_CODE = 76210
DATA = CurrentWeather()

def get_zipcode():
    #connect html page for the user to enter their current zip 
    return 0

def get_weather_data_by_location():
    #####################################
    #   Get lat, lon, and city name     #
    #####################################
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={ZIP_CODE}&appid={OPEN_WEATHER_MAP_APIKEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    lat = data["lat"]
    lon = data["lon"]
    city = data["name"]

    #####################################
    #        Get current weather       #
    #####################################
    url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_MAP_APIKEY}'
    cityResponse = requests.get(url2)
    weatherData = json.loads(cityResponse.text)

    DATA.Lon = lon
    DATA.Lat = lat
    DATA.City = city
    DATA.TempMin = data["temp_min"]
    DATA.TempMax = data["temp_max"]
    DATA.Temp = data["temp"]
    DATA.AtmoPressure = data["pressure"]
    DATA.Humidity = data["humidity"]
    DATA.Visibility = data["visibility"]

    return weatherData
    if response.status_code == 200:
        return response.json() 
    else:
        return None

if __name__ == '__main__':
    print("Getting Weather Data")
    print( get_weather_data_by_location() )
