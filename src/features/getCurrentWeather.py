#API Call Key:     http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
#ex.)     api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}
#    Response: { "cod": 429,"message": "Your account is temporary blocked due to exceeding of requests limitation of your subscription type. 
#                 Please choose the proper subscription http://openweathermap.org/price" }


###########################
#       Version 1         #
###########################

# import required modules
import requests, json

# Enter your API key here
api_key = "fed200574f31448d3c4ef74409fc60bf"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
city_name = input('Enter city name : ')

# complete_url variable to store
# complete url address
complete_url = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":

    # store the value of "main"
    # key in variable y
    y = x["main"]

    # store the value corresponding
    # to the "temp" key of y
    current_temperature = y["temp"]

    # store the value corresponding
    # to the "pressure" key of y
    current_pressure = y["pressure"]

    # store the value corresponding
    # to the "humidity" key of y
    current_humidity = y["humidity"]

    # store the value of "weather"
    # key in variable z
    z = x["weather"]

    # store the value corresponding
    # to the "description" key at
    # the 0th index of z
    weather_description = z[0]["description"]

    # print following values
    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
        "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
        "\n humidity (in percentage) = " +
                    str(current_humidity) +
        "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")

###########################
#       Version 2         #
###########################

OPEN_WEATHER_MAP_APIKEY = '8fd4b4bcadcb256004173dd55278a0da'

def get_weather_data_by_location( lat, long):
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={long}&appid={OPEN_WEATHER_MAP_APIKEY}&units=metric'
    print(f"Getting data via {url}")
    r = requests.get(url)
    return r.json()
    if r.status_code == 200:
        return r.json()
    else:
        return None

if __name__ == '__main__':
    print("Getting Weather Data")
    print( get_weather_data_by_location( '22.300910042194783', '114.17070449064359') )
