import scrapy
from stack.items import FinanceItem

  
class FinanceSpider(scrapy.Spider):
    name = 'finance'
    start_urls = []

    def __init__(self):
        page = 0
        subject_amount = int(input("\nEnter amount of stocks to scrape:\n"))
        page_strict = set() if input("\nAllow duplicates? (y/n)\n") == 'n' else 0

        while page < subject_amount:
            subject = input("\nEnter a stock symbol to scrape:\n").lower()
            if subject in page_strict:
                print("Stock already scraped, try again.")
                continue
            else:
                self.start_urls.append(f'https://finance.yahoo.com/quote/{subject}')
                page_strict.add(subject) if page_strict != 0 else None
                page += 1

    def parse(self, response):
        items = FinanceItem()

        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1').css('::text').get()
        items['previous_close'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]').css('::text').get()
        items['open'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]').css('::text').get()
        items['bid'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]').css('::text').get()
        items['ask'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]').css('::text').get()
        items['range_day'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]').css('::text').get()
        items['range_52weeks'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]').css('::text').get()
        items['volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]').css('::text').get()
        items['avg_volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]').css('::text').get()

        yield items