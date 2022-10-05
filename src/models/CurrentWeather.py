class weather:
    def init(self, Lat, Lon, City, Temp, TempMin, TempMax, AtmoPressure, Humidity):
        self.Lat = Lat
        self.Lon = Lon
        self.City = City
        self.Temp = Temp
        self.TempMin = TempMin
        self.TempMax = TempMax
        self.AtmpPressure = AtmoPressure
        self.Humidity = Humidity

def test(Lat, Lon, City, Temp, TempMin, TempMax, AtmoPressure, Humidity):
    print("hello world")