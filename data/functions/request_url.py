import json
import time
import random
import requests


def thread_test(model: str) -> json:
    with open('data/logs.txt', 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write('-------------------------------------------------------------\n')
        for i in range(1, 50):
            f.write(f'Attempt number {i}\n')
            temp_thread = requests.get(model).json()
            if temp_thread.get('status') == 'OK':
                # TODO
                f.write(f'{model} is uploaded\n')
                return temp_thread
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
    return None


def get_json_from_url(url: str) -> json:
    result: json = None
    with open('data/logs.txt', 'a', encoding='utf-8') as f:
        temp: json = requests.get(url).json()
        if temp.get('status') == 'OK':
            f.write(f'{url} has been uploaded\n')
            result = temp
        else:
            result = thread_test(url)
        time.sleep(2)
        f.close()
    return result
