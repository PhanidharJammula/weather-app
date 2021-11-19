import json
import pickle
import weather
import unittest
import random

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        weather.app.testing = True
        self.app = weather.app.test_client()

    def test_get_regions_and_parameters(self):
        response = self.app.get('/get_regions_and_parameters')
        response = json.loads(response.data.decode('UTF-8'))

        assert isinstance(response, dict)
        assert 'regions' in response
        assert 'parameters' in response
        regions_data = response['regions']
        parameters_data = response['parameters']
        assert isinstance(regions_data, list)
        assert isinstance(parameters_data, list)
    
    def test_weather_data(self):
        response = self.app.get('/')
        response = json.loads(response.data.decode('UTF-8'))
        assert isinstance(response, dict)

if __name__ == '__main__':
    unittest.main()
