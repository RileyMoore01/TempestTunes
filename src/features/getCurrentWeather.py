# import required modules
import requests, json

def get_zipcode():
    #connect html page for the user to enter their current zip code

def get_weather_data_by_location():
    #####################################
    #   Get lat, lon, and city name     #
    #####################################
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip}&appid={OPEN_WEATHER_MAP_APIKEY}'
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

    return weatherData
    if response.status_code == 200:
        return response.json() 
    else:
        return None

if __name__ == '__main__':
    print("Getting Weather Data")
    print( get_weather_data_by_location() )
