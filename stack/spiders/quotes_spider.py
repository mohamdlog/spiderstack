import scrapy
from stack.items import QuoteItems

  
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = []

    def __init__(self):
        page_amount = int(input("\nEnter amount of pages to scrape:\n"))
        page_strict = 0 
        if page_amount > 1:
            if input("\nAllow duplicates? (y/n)\n") == 'n':
                page_strict = set()

        for i in range(page_amount):
            page_number = 0
            while page_number < 1 or page_number > 10:
                page_number = int(input("\nEnter a page number to scrape: (1 - 10)\n"))
                if page_strict != 0 and page_number in page_strict:
                    print("Page number already scraped, try again.")
                    page_number = 0
                    continue
            else:
                self.start_urls.append(f'https://quotes.toscrape.com/page/{page_number}')
                page_strict.add(page_number) if page_strict != 0 else None
  
    def parse(self, response):
        for quote in response.css('div.quote'):
            items = QuoteItems()

            items['text'] = quote.css('span.text::text').get()
            items['author'] = quote.css('small.author::text').get()
            items['tags'] = quote.css('div.tags a.tag::text').getall()

            yield items
           