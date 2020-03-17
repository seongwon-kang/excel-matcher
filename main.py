from os import rename, walk
from pyexcel_xlsx import get_data
from re import match
import config

data = get_data(config.EXCEL_PATH)
test_regex = r"\d{4}-\d{2}-\d{2} \d{2} \d{2} \d{2}"
date = {}

for sheet in data:
    for row in data[sheet]:
        if len(row) > 1 and match(test_regex, row[-1]) is not None:
            dates = row[-1].split("\n")
            for dt in dates:
                date[dt] = row[0]
# for file in walk(config.DIRECTORY_PATH):
#     if date[file] != None:
#         rename(file, f"(date[file])" + file)

# for file in walk(config.DIRECTORY_PATH):
#     print(file)
