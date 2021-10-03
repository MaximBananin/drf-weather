from django.test import TestCase

from .services import get_particion_cities, get_index_for_city
from .services import request_weather_from_openweathermap
from .services import get_weather_from_chache


class ServicesTestCase(TestCase):
    def test_existin_city(self):
        index = get_index_for_city('Kosterevo')
        self.assertEqual(index, 461720)

    def test_not_existin_city(self):
        index = get_index_for_city('abcdefg')
        self.assertEqual(index, None)

    def test_city_hints(self):
        result = get_particion_cities('kosti')
        self.assertEqual(result, [b"Kostikov", b"Kostino"])

    def test_request_openweathermap(self):
        result = request_weather_from_openweathermap(461720)
        self.assertTrue(type(result) is type(dict()))
        self.assertEqual(result['name'], 'Kosterevo')

    def test_cache_weather(self):
        result = get_weather_from_chache(461720)
        self.assertTrue(type(result) is type(dict()))
        self.assertEqual(result['name'], 'Kosterevo')
