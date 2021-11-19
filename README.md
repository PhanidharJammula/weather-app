# weather-app
Provides weather data of regions based on given parameter through api.

****Setup & Run**

    docker build -t weather-app .
    docker-compose up -d

****API Details**


**documentation api**

    http://127.0.0.1:5000/documentation

**get regions and parameters**

    http://127.0.0.1:5000/get_regions_and_parameters

**get weather data of random region and parameter**

    http://127.0.0.1:5000/

**get weather data of specified region and paramater**

    http://127.0.0.1:5000/get_weather/UK/Tmean
