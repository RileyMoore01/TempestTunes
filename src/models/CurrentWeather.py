from typing_extensions import Self

class CurrentWeather:
    def init(Lat, Lon, City, Temp, TempMin, TempMax, AtmoPressure, Humidity, Visibility, Description):
        self.Lat = Lat
        Self.Lon = Lon
        self.City = City
        self.Temp = Temp
        self.TempMin = TempMin
        self.TempMax = TempMax
        self.AtmpPressure = AtmoPressure
        self.Humidity = Humidity
        self.Visibility = Visibility
        self.Description = Description

# def weather():
#     Lat = 0.0
#     Lon = 0.0
#     City = ""
#     Temp = 0.0
#     TempMin = 0.0
#     TempMax = 0.0
#     AtmoPressure = 0
#     Humidity = 0
#     Visibility = 0
#     Description = ""