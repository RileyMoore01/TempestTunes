# import required modules

import requests, json
from pickletools import long1

# import sys
# sys.path.append("../")
# from models.CurrentWeather import test

#Global variables
OPEN_WEATHER_MAP_APIKEY = 'fed200574f31448d3c4ef74409fc60bf'
ZIP_CODE = 76210

def get_zipcode():
    #connect html page for the user to enter their current zip
    return 0

def get_weather_data_by_location():
    ####################################
    #   Get lat, lon, and city name     #
    #####################################

    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={ZIP_CODE}&appid={OPEN_WEATHER_MAP_APIKEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    lat = data["lat"]
    lon = data["lon"]
    city = data["name"]

    #####################################
    #        Get current weather        #
    #####################################

    url2 = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_MAP_APIKEY}'
    cityResponse = requests.get(url2)
    weatherData = json.loads(cityResponse.text)

    Tempature = cellData["temp"]
    Tempature = 1.8 * (Tempature - 273) + 32    #Convert to fahrenheit

    TempMin = cellData["temp_min"]
    TempMin = 1.8 * (TempMin - 273) + 32    #Convert to fahrenheit

    TempMax = cellData["temp_max"]
    TempMax = 1.8 * (TempMax - 273) + 32    #Convert to fahrenheit

    cellData = weatherData["main"]
    Pressure = cellData["pressure"]
    Humidity = cellData["humidity"]


    print(Pressure)
    print(Humidity)

    #
    #  Send this data to determine which playlist to play here
    #

    return weatherData

    if response.status_code == 200:
        return response.json() 
    else:
        return None



if __name__ == '__main__':
    print("Getting Weather Data")
    get_weather_data_by_location()
