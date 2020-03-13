from os import rename, walk
from pyexcel_xlsx import get_data
import config

data = get_data(config.EXCEL_PATH)
date = {}

for sheet in data:
    for row in data[sheet]:
        if len(row) > 11:
            date[row[10]] = row[10]

for file in walk(config.DIRECTORY_PATH):
    if date[file] != None:
        rename(file, date[file])

# for file in walk(config.DIRECTORY_PATH):
#     print(file)
