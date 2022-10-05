class weather:
    def init(self, Lat, Lon, City, Temp, TempMin, TempMax, AtmoPressure, Humidity, Visibility, Description):
        self.Lat = Lat
        self.Lon = Lon
        self.City = City
        self.Temp = Temp
        self.TempMin = TempMin
        self.TempMax = TempMax
        self.AtmpPressure = AtmoPressure
        self.Humidity = Humidity
        self.Visibility = Visibility
        self.Description = Description

def test(Lat, Lon, City, Temp, TempMin, TempMax, AtmoPressure, Humidity, Visibility, Description):
    # newWeather = weather(Lat, Lon, City, Temp, TempMin, TempMax, AtmoPressure, Humidity, Visibility, Description)
    # return newWeather