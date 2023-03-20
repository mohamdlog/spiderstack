import os
import stack


path = input("Enter directory for new data_fetcher folder:\n") + "data_fetcher"
if not os.path.exists(path):
    os.makedirs(path)
if os.path.exists(path):
    print("Existing data_fetcher folder found, moving on.\n")

data = input("What type of data would you like?\n( quotes || books || )\n")

match data:
    case 'quotes':
        os.system("scrapy crawl quotes")
    case _:
        print("Invalid option, try again.")