from pathlib import Path
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    page_set = set()
    page_amount = int(input("Enter amount of pages to scrape: (1 - 10)\n"))

    start_urls = []
    
    for i in range(page_amount):
        page_number = 0

        while page_number < 1 or page_number > 10:
            page_number = int(input("Enter a page number to scrape: (1 - 10)\n"))
            if page_number in page_set:
                print("Page number already scraped, try again.")
                page_number = 0
                continue
        else:
            start_urls.append('https://quotes.toscrape.com/page/' + str(page_number))
            page_set.add(page_number)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')