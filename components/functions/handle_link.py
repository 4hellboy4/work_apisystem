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


def handle_offer_link(model: str, level: int, file: json, params, json_list: JsonList) -> None:
    #TODO - add parameters of type dict
    if file['status'] != 'OK':
        return
    if 'filters' in file:
        if level == -1:
            params = {}
            params['others'] = {}
        temp = file['filters']
        keys_list: list = [key for key in temp.keys()]
        level += 1
        if level == len(keys_list):
            # process_link(model, params, 'specification')
            add_to_json_list(process_link(model, params, 'specification'), json_list)
            return
        for key in file['filters'][keys_list[level]]['valueIds']:
            name = temp[keys_list[level]]['name']
            sku_id: str = temp[keys_list[level]]['valueIds'][key]['skuId']
            value: str = temp[keys_list[level]]['valueIds'][key]['value']
            params['others'][name] = value
            url: str = f'http://market.apisystem.name/models/{model}/offers?&format=json&skuid={sku_id}&api_key={api_key}'
            handle_offer_link(model, level, get_json_from_url(url), params, json_list)
    else:
        pass










