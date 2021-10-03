from django.urls import path

from .views import CityView, WeatherView


urlpatterns = [
    path('city/', CityView.as_view()),
    path('weather/', WeatherView.as_view()),

]
