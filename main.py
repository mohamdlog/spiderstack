import shutil
import glob
import os
from pathlib import Path


path = None
create = input("Create folder to store data? (y/n) ")
if create == 'y':
    path = input("\nEnter path for new folder:\n") + "scraped_data/"
    if os.path.exists(path):
        print("Existing data_fetcher folder found, continuing.")
    if not os.path.exists(path):
        os.makedirs(path)

data = input("\nSelect subject to start scraping.\n( quotes || wikipedia || )\n")
ext = None

match data:
    case 'quotes':
        os.system("scrapy crawl quotes -O quotes.json")
        ext = '\*.json'
    case 'wikipedia':
        os.system("scrapy crawl wikipedia")
        ext = ''
    case _:
        print("Invalid option, try again.")

if path is not None:
    files = glob.iglob(f'{Path()}{ext}')
    for file in files:
        file_name = os.path.basename(file)
        shutil.move(file, f'{path}{file_name}')