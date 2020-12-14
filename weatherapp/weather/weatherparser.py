from weather.TemperatureConverter import TemperatureConverter
class WeatherParser:
    
    def __init__(self):
        self.__temp_converter = TemperatureConverter()

    def get_parsed_weather_data(self, rawData):
        current_temp = self.__get_current_temp(rawData)
        wind_speed = self.__get_wind_speed(rawData)
        max_temp = self.__get_max_temp(rawData)
        min_temp = self.__get_min_temp(rawData)
        weather_description = self.__get_weather_description(rawData)
        city_name = self.__get_city_name(rawData)

        return (city_name,current_temp,wind_speed,min_temp,max_temp,weather_description,) 
    


    def __get_current_temp(self,data):

        return self.__temp_converter.get_temp_in_celsius(data['main']['temp'])
        

    def __get_wind_speed(self, data):
        return data['wind']['speed']

    def __get_max_temp(self, data):
        return self.__temp_converter.get_temp_in_celsius(data['main']['temp_max'])
    
    def __get_min_temp(self, data):
        return self.__temp_converter.get_temp_in_celsius(data['main']['temp_min'])

    def __get_weather_description(self, data):
        return data['weather'][0]['description']
    
    def __get_city_name(self, data):
        return data['name']
    



