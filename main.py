import os
import scrapy
from pathlib import Path

permission = input("Would you like to create a new folder for data_fetcher? (y/n)\n")
if permission == "y":
    newpath = input("Enter directory for new data_fetcher folder:\n") + "data_fetcher"
    if not os.path.exists(newpath):
        os.makedirs(newpath)