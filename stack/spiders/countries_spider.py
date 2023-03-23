import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    start_urls = ['https://www.scrapethissite.com/pages/simple/']
    country_amount = int(input("\nEnter amount of countries to scrape:\n"))
    page_strict = set() if input("\nAllow duplicates? (y/n)\n") == 'n' else 0

    for i in range(country_amount):
        page_number = 0

        while page_number < 1 or page_number > 10:
            page_number = int(input("\nEnter a page number to scrape: (1 - 10)\n"))
            if page_strict != 0 and page_number in page_strict:
                print("Page number already scraped, try again.")
                page_number = 0
                continue
        else:
            start_urls.append(f'https://quotes.toscrape.com/page/{page_number}')
            page_strict.add(page_number) if page_strict != 0 else None
    
    def parse(self, response):
        for countryinfo in response.css('div.country-info'):
            yield {
                'country_name': countryinfo.css('span.text::text').get(),
                'author': countryinfo.css('small.author::text').get(),
                'tags': countryinfo.css('div.tags a.tag::text').getall(),
            }