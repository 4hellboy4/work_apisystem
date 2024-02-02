import json


class JsonList:
    def __init__(self):
        self.items: list[json] = []


def init_json_list() -> JsonList:
    return JsonList()