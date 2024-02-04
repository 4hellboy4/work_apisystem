import json

from components.functions.request_url import get_json_from_url


def process_link(model_id: str, t_dict: dict, count: int) -> json:
    api_key: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'
    link_product: str = f'http://market.apisystem.name/models/{model_id}/specification?&format=json&api_key={api_key}'
    link_offers: str = f'http://market.apisystem.name/models/{model_id}/offers?&format=json&api_key={api_key}'

    prod_characteristics = get_json_from_url(link_product)

    prod_offers = get_json_from_url(link_offers)

    t_dict.update(prod_characteristics)
    t_dict.update(prod_offers)

    with open(f'data/draft_files/draft_{count}.json', 'w', encoding='utf-8') as file:
        json.dump(t_dict, file, ensure_ascii=False)
        file.close()

    return t_dict
