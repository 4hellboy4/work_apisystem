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


def thread_test(model: str, cnt: int) -> None:
    with open('data/logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('-------------------------------------------------------------\n')
        for i in range(1, 100):
            f.write(f'Attempt number {i}\n')
            temp_thread = requests.get(model).json()
            if temp_thread.get('status') == 'OK':
                with open(f'data/json_test/{cnt}_offer.json', 'w', encoding='utf-8') as file:
                    json.dump(temp_thread, file, indent=4, ensure_ascii=False)
                    file.close()
                f.write(f'{cnt}) {model} is uploaded\n')
                break
            elif temp_thread.get('status') == 'ERROR':
                f.write(f'----{model} gor ERROR----\n')
                break
            else:
                time.sleep(random.uniform(0.7, 1.5))
                f.write(f'{temp_thread.get("status")}\n')
                continue
        f.write('-------------------------------------------------------------\n')
        f.write('\n')
        f.close()


def upload_files() -> None:
    with open('data/logs.txt', 'a', encoding='utf-8') as f:
        cnt: int = 1
        for model in list_of_IDs:
            if cnt % 200 == 0:
                time.sleep(100)
            temp = requests.get(model).json()
            if temp.get('status') == 'OK':
                with open(f'data/json_test/{cnt}_offer.json', 'w', encoding='utf-8') as file:
                    json.dump(temp, file, indent=4, ensure_ascii=False)
                    file.close()
                f.write(f'{cnt}) {model} is uploaded\n')
            else:
                thread_test(model, cnt)
            time.sleep(2)
            cnt += 1
        f.close()


def main() -> None:
    init_list()

    upload_files()


if __name__ == '__main__':
    main()
