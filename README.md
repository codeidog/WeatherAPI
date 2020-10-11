# WeatherAPI
## Configuration
The config.yaml shuld look like so:  
```
Key: "fsfsfsfd"  
#Dev or Prod  
Mode: "prod"
```
* Key - for authentication with the Open Weather API
* Mode - Prod for sending requests driectly to the Open Weather API  
         Dev for mocking the server with UnitTest

Currently there is only one request available for `/data/2.5/weather`. The script will access current weather data for a specific city.

Default mock response file is `weather_by_city.json`