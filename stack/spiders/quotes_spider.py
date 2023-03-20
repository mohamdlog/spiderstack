from pathlib import Path
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_n = 0

    while page_n < 1 or page_n > 10:
        page_n = int(input("Enter page number to scrape: (1 - 10)\n"))

    url = ['https://quotes.toscrape.com/page/3']

    def parse(self, response):
        page = response.url
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')