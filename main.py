import json

from components.classes.json_list import init_json_list, JsonList
from components.functions.pars_offers import pars_file
from components.functions.init_logs import init_logs

API_KEY: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'


def main() -> None:
    list_json: JsonList = init_json_list()
    init_logs()
    pars_file(list_json)

    with open('data/draft_files/draft1.json', 'w', encoding='utf-8') as f:
        json.dump(list_json.items, f, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
