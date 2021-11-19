# weather-app
Provides weather data of regions based on given parameter through api.

**Install Docker**

    sudo apt-get update
    sudo apt-get install \
        apt-transport-https \
        ca-certificates \
        curl \
        gnupg \
        lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo \
      "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install docker-ce docker-ce-cli containerd.io
    apt-cache madison docker-ce

    sudo groupadd docker
    sudo usermod -aG docker $USER
    newgrp docker 

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
