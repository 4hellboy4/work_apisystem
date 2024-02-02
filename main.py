import json
import random
import time

import requests

API_KEY: str = '0c8bd89c2e517164204ceb1dfee65289a659b4bcffee'

list_of_IDs: list[str] = []


# def test() -> None:
#     for elem in list_of_IDs:
#         print(get_link(elem))


def init_list() -> None:
    with open('data/IDs.txt', 'r') as file:
        for id_file in file:
            list_of_IDs.append(id_file.strip())


def upload_directly(link: str, id: str) -> None:
    print('-' * 40)
    for i in range(40):
        r = requests.get(link).json()
        print(f'attempt number {i+1}')
        if r.get('status') == 'OK':
            with open(f'data/json_test/{id}_offer.json', 'w', encoding='utf-8') as file:
                json.dump(r, file, indent=4, ensure_ascii=False)
            print(f'done with {id} parsing')
            break
        print(r.get('status'))
        time.sleep(random.uniform(0.5, 1.5))


def thread_test(model: str, cnt: int) -> None:
    print()
    print('-' * 40)
    for i in range(1, 100):
        print(f'Attempt number {i}')
        temp_thread = requests.get(model).json()
        if temp_thread.get('status') == 'OK':
            with open(f'data/json_test/{cnt}_offer.json', 'w', encoding='utf-8') as file:
                json.dump(temp_thread, file, indent=4, ensure_ascii=False)
            print(f'{cnt}) {model} is uploaded')
            break
        elif temp_thread.get('status') == 'ERROR':
            print(f'----{model} gor ERROR----')
            break
        else:
            time.sleep(random.uniform(0.7, 1.5))
            print(temp_thread.get('status'))
            continue
    print('-' * 40)
    print()


def upload_files() -> None:
    cnt: int = 1
    for model in list_of_IDs:
        if cnt % 250 == 0:
            time.sleep(200)
        temp = requests.get(model).json()
        if temp.get('status') == 'OK':
            with open(f'data/json_temp/{cnt}_offer.json', 'w', encoding='utf-8') as file:
                json.dump(temp, file, indent=4, ensure_ascii=False)
            print(f'{cnt}) {model} is uploaded')
        else:
            thread_test(model, cnt)
        time.sleep(2)
        cnt += 1


def main() -> None:
    init_list()

    upload_files()


if __name__ == '__main__':
    main()
