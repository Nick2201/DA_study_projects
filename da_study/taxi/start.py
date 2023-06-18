import pandas as pd
from pathlib import Path
df = pd.read_csv(r'bookings.csv',sep=';')


with open('Описание.md', 'r', encoding="utf-8") as f:
    _data = [_row.replace('\n','').rstrip().split(' – ') for _row in f.readlines()[2:]]
    data_desc = pd.DataFrame(_data)

