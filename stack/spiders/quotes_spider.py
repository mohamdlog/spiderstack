from pathlib import Path
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    page_n = 0

    while page_n < 1 or page_n > 10:
        page_n = int(input("Enter page number to scrape: (1 - 10)\n"))

    start_urls = ['https://quotes.toscrape.com/page/' + str(page_n)]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        Path(filename).write_bytes(response.body)
        self.log(f'Saved file {filename}')