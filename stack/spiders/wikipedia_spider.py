import scrapy
from stack.items import WikipediaItems


class WikipediaSpider(scrapy.Spider):
    name = 'wikipedia'
    start_urls = []

    def __init__(self):
        page = 0
        page_amount = int(input("\nEnter amount of subjects to scrape:\n"))
        page_strict = 0 
        if page_amount > 1:
            if input("\nAllow duplicates? (y/n)\n") == 'n':
                page_strict = set() 

        while page < page_amount:
            subject = input("\nEnter a subject to scrape (needs to be a specific subdirectory):\n").lower()
            if page_strict != 0 and subject in page_strict:
                print("Subject already scraped, try again.")
                continue
            else:
                self.start_urls.append(f'https://en.wikipedia.org/wiki/{subject}')
                page_strict.add(subject) if page_strict != 0 else None
                page += 1

    def parse(self, response):
        items = WikipediaItems()

        items['subject_name'] = response.xpath('//*[@id="firstHeading"]/span//text()').get()
        items['subject_intro'] = "".join(response.xpath('//*[@id="mw-content-text"]/div[1]/p[2]//text()').getall())

        yield items