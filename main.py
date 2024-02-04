from components.classes.json_list import init_json_list, JsonList
from components.functions.pars_offers import pars_file
from components.functions.init_logs import init_logs
from components.functions.pars_to_csv import upload_to_csv


API_KEY: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'


def main() -> None:
    list_json: JsonList = init_json_list()
    init_logs()
    pars_file(list_json)
    upload_to_csv(list_json)


if __name__ == '__main__':
    main()
