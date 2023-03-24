import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wikipedia'
    start_urls = []

    def __init__(self):
        page = 0
        subject_amount = int(input("\nEnter amount of subjects to scrape:\n"))
        page_strict = set() if input("\nAllow duplicates? (y/n)\n") == 'n' else 0

        while page < subject_amount:
            subject = input("\nEnter a subject to scrape (needs to be a specific subdirectory):\n").lower()
            if subject in page_strict:
                print("Page number already scraped, try again.")
                continue
            else:
                self.start_urls.append(f'https://en.wikipedia.org/wiki/{subject}')
                page_strict.add(subject) if page_strict != 0 else None
                page += 1

    def parse(self, response):
        pass