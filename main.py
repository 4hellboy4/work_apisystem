import json
import time

from components.classes.json_list import init_json_list, JsonList
from components.functions.pars_offers import pars_file
from components.functions.init_logs import init_logs
from components.functions.pars_to_csv import upload_to_csv
from components.functions.request_url import get_json_from_url
from components.constants.api_key import api_key
from components.functions.handle_link import handle_link
'''
Алгоритм:
1)Переходим сначала по ссылке и смотрим есть ли фильтры.
    1. Если есть фильтры то мы получается делаем другие запросы и смотрим спесификации всех товаров по отдельности
    2. Если нет, то мы созраняем этот запрос и делаем обычный чтобы посмотреть спесификации 
'''


def main() -> None:
    st = time.time()
    goods = set()
    json_class: JsonList = init_json_list()
    scan = '1873868214'
    link: str = f'http://market.apisystem.name/models/{scan}/offers?&format=json&api_key={api_key}'
    handle_link(scan, 0, get_json_from_url(link), json_class, goods)

    # print()
    # cnt = 1
    # for good in goods:
    #     print(f'{cnt}) {good}')
    #     cnt+=1
    #
    # print()
    print(len(goods))
    print(time.time() - st)

    # upload_to_csv(json_class)

    # scan = input()
    # cnt = 1
    # while scan != 'stop':
    #     link: str = f'http://market.apisystem.name/models/{scan}/offers?&format=json&api_key={api_key}'
    #     with open(f'data/jsons/product_spec_{cnt}.json', 'w',  encoding='utf-8') as file:
    #         json.dump(get_json_from_url(link), file, ensure_ascii=False, indent=4)
    #         file.close()
    #     link: str = f'http://market.apisystem.name/models/{scan}/offers?&format=json&api_key={api_key}'
    #     with open(f'data/jsons/product_offers_{cnt}.json', 'w',  encoding='utf-8') as file:
    #         json.dump(get_json_from_url(link), file, ensure_ascii=False, indent=4)
    #         file.close()
    #     cnt+=1
    #     print('\n go on \n')
    #     scan = input()




if __name__ == '__main__':
    main()
