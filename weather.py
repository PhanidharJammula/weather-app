import random
import requests

from flask import Flask, jsonify
from flask_autodoc.autodoc import Autodoc

app = Flask(__name__)
auto = Autodoc(app)


metoffice_base_url = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/'
regions = ['UK', 'England', 'Wales', 'Scotland', 'Northern_Ireland', \
           'England_and_Wales', 'England_N', 'England_S', 'Scotland_N', \
           'Scotland_E', 'Scotland_W', 'England_E_and_NE' , \
           'England_NW_and_N_Wales', 'Midlands', 'East_Anglia', \
           'England_SW_and_S_Wales','England_SE_and_Central_S']
parameters = ['Tmax', 'Tmin', 'Tmean', 'Sunshine', 'Rainfall', \
              'Raindays1mm', 'AirFrost']


@auto.doc()
@app.route('/get_regions_and_parameters', methods = ['GET', 'POST'])
def get_regions_and_parameters():
    """Gives the regions & paramaters list to get weather info"""
    return jsonify({'regions': regions, 'parameters': parameters})

@auto.doc()
@app.route('/', methods = ['GET', 'POST'])
@app.route('/get_weather/<region>/<param>', methods = ['GET', 'POST'])
def get_weather_info(region=None, param=None):
    """Gives the information of provided region and param, if not provided \
        returns random region and param weather data"""
    if not param:
        param = random.choice(parameters)
    
    if not region:
        region = random.choice(regions)
 
    url = metoffice_base_url + param + '/date/' + region + '.txt'
    response = requests.get(url)
    data = response.text
    parsed_data = data.split('\n')

    key = 'weather data of ' + region + ' and parameter is ' + param
    
    return jsonify({key: parsed_data})

@app.route('/documentation')
def documentation():
    return auto.html()

  
if __name__ == '__main__':  
    app.run(debug = True, host='0.0.0.0')
