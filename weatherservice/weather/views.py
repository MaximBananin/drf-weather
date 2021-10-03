from rest_framework.views import APIView
from rest_framework.response import Response#, JSONResponse
from rest_framework.parsers import FileUploadParser

from .services import get_particion_cities, get_index_for_city
from .services import request_weather_from_openweathermap
from .services import get_weather_from_chache


class CityView(APIView):
    """
    API endpoint get cities list.
    """
    def post(self, request):  #{"chars":"kos"}
        cities = get_particion_cities(request.data['chars'])
        if cities:
            return Response(cities)
        return Response('Error. Patern mach not found.', status=404)


class WeatherView(APIView):
    """
    API endpoint take city name and returns the weather.
    """
    def post(self, request):  #{"city":"Kosterevo"}
        city = request.data['city']
        index = get_index_for_city(city)
        if not index:
            return Response('Error. City not found', status=404)

        data = get_weather_from_chache(index)
        if not data:
            data = request_weather_from_openweathermap(index)

        return Response(data, status=200)
