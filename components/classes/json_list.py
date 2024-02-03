import json


class JsonList:
    def __init__(self):
        self.items: list[dict] = []


def init_json_list() -> JsonList:
    return JsonList()


def add_to_json_list(json_item: dict, json_list: JsonList) -> None:
    json_list.items.append(json_item)
