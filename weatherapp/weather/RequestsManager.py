import requests


class RequestsManager:
    def __init__(self):
        self.__key = 'e95aa78f4d2240385be6cfec4e783f58'
        self.__url = "http://api.openweathermap.org/data/2.5/weather?"

    def make_request(self,city_name):
        payload = {"q":city_name,"appid": self.__key}
        service_data = requests.get(self.__url, payload)
        if service_data.status_code == 200:
            return service_data.json()
        else:
            return None

