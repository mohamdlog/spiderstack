import shutil
import glob
import os
from pathlib import Path


path = None
create = input("Create folder to store data? (y/n)\n")
if create == 'y':
    path = input("\nEnter path for new folder:\n") + input("Enter name for new folder:\n")
    if os.path.exists(path):
        print("Folder in path exists, continuing.")
    if not os.path.exists(path):
        os.makedirs(path)

ext = input("\nEnter export type:\n( JSON || JSONL || CSV || XML )\n").lower()
data = input("\nEnter subject to start scraping:\n( quotes || wikipedia || finance )\n").lower()

match data:
    case 'quotes':
        os.system(f'scrapy crawl quotes -O quotes.{ext}')
    case 'wikipedia':
        os.system(f'scrapy crawl wikipedia -O wikipedia.{ext}')
    case 'finance':
        os.system(f'scrapy crawl finance -O finance.{ext}')
    case _:
        print("Invalid option, try again.")

if path is not None:
    files = glob.iglob(f'{Path()}/*.{ext}')
    for file in files:
        file_name = os.path.basename(file)
        shutil.move(file, f'{path}/{file_name}')

print((f'\n{data}.{ext} has been stored in ') + ("spiderstack directory" if path is None else path) + '.\n')