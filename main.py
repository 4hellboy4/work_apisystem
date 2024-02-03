import json
import random
import time
import requests
from data.classes.json_list import init_json_list, JsonList
from data.functions.pars_offers import pars_file
from data.functions.init_logs import init_logs

API_KEY: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'


def main() -> None:
    # list_json: JsonList = init_json_list()
    init_logs()
    pars_file()


if __name__ == '__main__':
    main()
