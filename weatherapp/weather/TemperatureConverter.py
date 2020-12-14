class TemperatureConverter:
    
    def get_temp_in_celsius(self, temp_in_kelvin):
        return  float(round(temp_in_kelvin - 273, 2))
