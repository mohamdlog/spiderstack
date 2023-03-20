import os
import stack
import scrapy


permission = input("Do you have an existing output folder for data_fetcher? (y || n)\n")
if permission == "n":
    newpath = input("Enter directory for new output folder for data_fetcher:\n") + "data_fetcher"
    if not os.path.exists(newpath):
        os.makedirs(newpath)

data = input("What type of data would you like?\n( quotes || books || )\n")

match data:
    case 'quotes':
        os.system("scrapy crawl quotes")
    case _:
        print("Invalid option, try again.")