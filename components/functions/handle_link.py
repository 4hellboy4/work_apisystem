import json

from components.functions.request_url import get_json_from_url
from components.functions.process_link import process_link
from components.constants.api_key import api_key
from components.classes.json_list import JsonList, add_to_json_list
'''
Алгоритм:
1)Переходим сначала по ссылке и смотрим есть ли фильтры.
    1. Если есть фильтры то мы получается делаем другие запросы и смотрим спесификации всех товаров по отдельности
        Мы получаем первый фильтр, там лежит значение и ссылка скю айди
    2. Если нет, то мы созраняем этот запрос и делаем обычный чтобы посмотреть спесификации
'''

def handle_link(model_id: str, level: int, req: json, jsons_list: JsonList, goods: set) -> None:
    # print(req['product_name'])
    if req['status'] != 'OK':
        return
    if 'filters' in req:
        keys_list: list[str] = [key for key in req['filters'].keys()]
        if level == len(keys_list):
            if req['product_name'] not in goods:
                add_to_json_list(req, jsons_list)
                print(req['product_name'])
                goods.add(req['product_name'])
            return
        temp_key: str = keys_list[level]
        for value_id in req['filters'][temp_key]['valueIds'].keys():
            sku_id: str = req['filters'][temp_key]['valueIds'][value_id]['skuId']
            value: str = req['filters'][temp_key]['valueIds'][value_id]['value']
            name = req['filters'][temp_key]['name']
            url: str = (f'http://market.apisystem.name/models/{model_id}/offers?&format=json&skuid={sku_id}&api_key={api_key}')
            handle_link(model_id, level + 1, get_json_from_url(url), jsons_list, goods)