from pathlib import Path
import shutil
import glob
import stack
import os


path = input("Enter directory for new data_fetcher folder:\n") + "data_fetcher"
if os.path.exists(path):
    print("Existing data_fetcher folder found, moving on.\n")
if not os.path.exists(path):
    os.makedirs(path)

data = input("What type of data would you like?\n( quotes || books || )\n")

match data:
    case 'quotes':
        os.system("scrapy crawl quotes")
    case _:
        print("Invalid option, try again.")