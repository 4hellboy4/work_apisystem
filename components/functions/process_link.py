import json

from components.functions.request_url import get_json_from_url


def process_link(model_id: str, t_dict: dict, flag: str) -> json:
    api_key: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'
    link_product: str = f'http://market.apisystem.name/models/{model_id}/specification?&format=json&api_key={api_key}'
    link_offers: str = f'http://market.apisystem.name/models/{model_id}/offers?&format=json&api_key={api_key}'

    if flag == 'specification':
        prod_characteristics = get_json_from_url(link_product)
        t_dict.update(prod_characteristics)
    elif flag == 'offers':
        prod_offers = get_json_from_url(link_offers)
        t_dict.update(prod_offers)
    else:
        prod_characteristics = get_json_from_url(link_product)
        t_dict.update(prod_characteristics)
        prod_offers = get_json_from_url(link_offers)
        t_dict.update(prod_offers)

    return t_dict
