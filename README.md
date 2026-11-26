# Sprint_10.1

UI-автотесты для сервиса Яндекс Маршруты: построение маршрута, точки на карте, выбор способа передвижения и заказ такси.

Сайт: https://qa-routes.education-services.ru/

## Структура

conftest.py        # фикстуры: driver (Chrome) и страницы (main_page, order_page)
urls.py            # адрес сервиса
data.py            # тестовые данные: адреса, тарифы, их id и ожидаемые значения
locators/          # локаторы главной страницы и окна заказа
pages/             # Page Object: base, main, order
tests/             # тесты выбора и отрисовки маршрута, подготовки и заказа такси
requirements.txt   # зависимости проекта
