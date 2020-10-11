import json
import requests
from .Constants import *
class Weather:
    ''' Sends request to the Open Weather API - https://openweathermap.org/api'''
    def __init__(self,key):
        self.key = key        
    def weather_by_city(self,city):        
        url = "{}/data/2.5/weather?q={}&appid={}".format(BASE_URL,city,self.key)
        response = requests.get(url)        
        return response