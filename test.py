import unittest
import yaml
from unittest.mock import Mock, patch
from Weather import Weather
import json
import os
class Tests(unittest.TestCase):
    def test_Weather_By_City(self):
        #Load configuration
        settings = load_config()        
        #Configure mocking if mode is development
        if(settings['Mode'].lower() == 'dev'):
            mock_get_patcher = patch('Weather.requests.get')
            mock_get = mock_get_patcher.start()
            mock_get.return_value.ok = True
            #Set the return value
            with open('weather_by_city.json','r') as jsonFile:
                jsonWeather = json.load(jsonFile)
                mock_get.return_value = Mock(ok=True)
                mock_get.return_value.json.return_value = jsonWeather
        weather = Weather(str(settings['Key']))
        response = weather.weather_by_city('Jerusalem')
        print (response.json())
        self.assertTrue(response.ok)    

    
def load_config():
        with open(os.path.join("config.yaml"),'r') as stream:
            settings = yaml.load(stream,Loader=yaml.FullLoader)
            return settings



if __name__ == '__main__':
    unittest.main()