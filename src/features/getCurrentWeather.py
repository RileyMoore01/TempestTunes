#API Call Key:     http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
#ex.)     api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
#    Response: { "cod": 429,"message": "Your account is temporary blocked due to exceeding of requests limitation of your subscription type. 
#                 Please choose the proper subscription http://openweathermap.org/price" }

# import required modules
import requests, json

OPEN_WEATHER_MAP_APIKEY = 'fed200574f31448d3c4ef74409fc60bf'
zip = 76210

def get_weather_data_by_location():
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip}&appid={OPEN_WEATHER_MAP_APIKEY}'
    response = requests.get(url)
    data = json.loads(response.text)

    lat = data["lat"]
    lon = data["lon"]
    city = data["name"]

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
