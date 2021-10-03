"""
Script for fill the redis.
Take data from "weather/resources/cityall.json"
Posible configure country_list.
"""

import json
import redis


r = redis.Redis()

country_list = ('RU',)
resulte = dict()

with open('weather/resources/cityall.json') as f:
    data = json.loads(f.read())
    for city in data:
        if city['country'] in country_list:
            resulte[city['name']] = city['id']

r.mset(resulte)
print(f'Success append {len(resulte)} cities')
