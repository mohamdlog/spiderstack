import shutil
import glob
import os
from pathlib import Path
from stack.items import CountryItem


path = input("Enter directory for new data_fetcher folder:\n") + "data_fetcher/"
if os.path.exists(path):
    print("Existing data_fetcher folder found, continuing.\n")
if not os.path.exists(path):
    os.makedirs(path)

data = input("What subject would you like data of?\n( quotes || countries || )\n")
ext = None

match data:
    case 'quotes':
        os.system("scrapy crawl quotes -O quotes.json")
        ext = '\*.json'
    case 'countries':
        os.system("scrapy crawl countr")
    case _:
        print("Invalid option, try again.")


files = glob.iglob(f'{Path()}{ext}')
for file in files:
    file_name = os.path.basename(file)
    shutil.move(file, f'{path}{file_name}')