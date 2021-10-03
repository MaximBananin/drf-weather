import requests
import redis

from django.conf import settings
from django.core.cache import cache



redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT,
                                   db=0)


def get_particion_cities(chars : str):
    """
    Internal services. The returned list corresponds to the name of the template city.
    """
    patern = chars.capitalize() + '*'
    resulte = redis_instance.keys(patern)
    return resulte


def get_index_for_city(city : str):
    """
    Internal services. The returned city_id corresponds to the name city.
    """
    city_id = redis_instance.get(city)
    if city_id:
        return int(city_id)
    return None


def request_weather_from_openweathermap(city_id : int):
    """
    External request services. The returned information from OpenWeatherMap.

    Data scheme: {'coord': {'lon': FLOAT, 'lat': FLOAT},
    'weather': [{'id': INT, 'main': 'STRING', 'description': 'STR', 'icon': 'BYTE'}],
    'base': 'STRING',
    'main': {'temp': FLOAT, 'feels_like': FLOAT, 'temp_min': FLOAT, 'temp_max': FLOAT,
             'pressure': INT, 'humidity': INT, 'sea_level': INT, 'grnd_level': INT},
    'visibility': INT,
    'wind': {'speed': FLOAT, 'deg': INT, 'gust': INT},
    'clouds': {'all': INT},
    'dt': INT,
    'sys': {'country': 'STR', 'sunrise': INT, 'sunset': INT},
    'timezone': INT,
    'id': INT,
    'name': 'STR',
    'cod': INT}
    """
    response = requests.get(url='https://api.openweathermap.org/data/2.5/weather',
                            params={'id':city_id, 'appid':settings.WEATHER_API_KEY})
    if not response.status_code == 200:
        return None
    weather = response.json()
    cache.set(city_id, weather, timeout=settings.CACHE_TTL)
    return weather


def get_weather_from_chache(index : int):
    """
    Internal services. The returned JSON weather from cache.
    """
    return cache.get(index)
