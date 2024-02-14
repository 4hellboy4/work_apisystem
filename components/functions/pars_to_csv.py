import csv
from pprint import pprint

import pandas as pd

from components.classes.json_list import JsonList


def upload_to_csv(json_list: JsonList) -> None:
    try:
        df_cleaned = pd.DataFrame(json_list.items)
        df_cleaned.index += 1
        df_cleaned.to_csv('data/csv_files/draft2.csv', quoting=csv.QUOTE_ALL, float_format="%.0f", encoding='utf-8',
                          index=True)
    except Exception as e:
        print(f"Error: {e}")
