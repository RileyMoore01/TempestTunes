from enum import Enum

class Weather(Enum):
    Sunny = 1
    Rainy = 2
    Snowy = 3
    Cloudy = 4

for i in Weather:
    print(i)