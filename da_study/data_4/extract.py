from pathlib import Path
from functools import cache
import_data_path = Path(r'D:\4. Programming\ProjectsSoftware\da_study\da_study\data_4\data\data')
@cache
def parse_folders_date(_path):
    
    big_list = []
    for folder_date in list(import_data_path.iterdir()):
        _list_folder_date = []
        _date = folder_date.name

        for folder_name in folder_date.iterdir():
            name = folder_name.name

            for folder_data in folder_name.iterdir():
                with open(folder_data,'r') as f:

                    for i in (f.read().splitlines()):
                        if 'product_id' not in i:

                            _list_folder_date.append([_date,name]+i.split(','))
        big_list.extend(_list_folder_date)
    return big_list

data = (parse_folders_date(import_data_path))
print(data)