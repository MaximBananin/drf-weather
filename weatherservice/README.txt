Проект "СервисПогоды" содержит приложение "Погода"
Приложение Погода использует openweathermap для получения информации.

Для запуска проекта необходимо заполнить редис сервер списком городов с ассоциироваными
индексами. Для этого предусмотрен скрипт init_data_manager.py.
Он использует ресурс-файл загруженый с openweathermap.org
Минимальная конфигурация: в файл настроек вписать свой API-key openweathermap переменную WEATHER_API_KEY

Приложение "Погода" имеет слудующие endpoints:
'city/' Принимает POST с параметром "chars", возвращает список городов
начинающихся с данного набора букв.

'weather/' Принимает POST с параметром "city", возвращает данные о погоде.


Примечания для ревьюера содержатся в testREADMI.txt
