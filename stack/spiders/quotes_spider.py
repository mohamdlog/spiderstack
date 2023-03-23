from pathlib import Path
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = []
    page_amount = int(input("Enter amount of pages to scrape: (1 - 10)\n"))
    page_strict = set() if input("Allow duplicates? (y/n)\n") == 'n' else 0

    for i in range(page_amount):
        page_number = 0

        while page_number < 1 or page_number > 10:
            page_number = int(input("Enter a page number to scrape: (1 - 10)\n"))
            if page_strict != 0 and page_number in page_strict:
                print("Page number already scraped, try again.")
                page_number = 0
                continue
        else:
            start_urls.append(f'https://quotes.toscrape.com/page/{page_number}')
            page_strict.add(page_number) if page_strict != 0 else None
    
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }