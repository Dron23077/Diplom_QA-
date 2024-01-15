# Коровников Андрей, 12-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests


# Создание зака за
def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         params=body).json()


# Поиск заказа по треку
def find_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_NUMBER,
                        params={'t': track_number})
