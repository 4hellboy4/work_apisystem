import csv
import json
import pandas as pd

all_jsons: list[json] = []


def gather_files() -> None:
    for i in range(1, 501):
        parse_file(i)


def parse_file(id: int) -> None:
    with open(f'data/jsons/{id}_offer.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        file.close()
    all_jsons.append(data)


def upload_to_csv() -> None:
    df_cleaned = pd.json_normalize(all_jsons)
    df_cleaned.index += 1

    df_cleaned.to_csv('data/csv_files/draft5.csv', quoting=csv.QUOTE_ALL, encoding='utf-8', index=True)

def main() -> None:
    gather_files()
    upload_to_csv()


if __name__ == '__main__':
    main()