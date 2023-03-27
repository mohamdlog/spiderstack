import os
import scrapy
from stack.items import FinanceItem

  
class FinanceSpider(scrapy.Spider):
    name = 'finance'
    start_urls = []

    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        page = 0
        page_amount = int(input("\nEnter amount of stocks to scrape:\n"))
        page_strict = 0 
        if page_amount > 1:
            if input("\nAllow duplicates? (y/n)\n") == 'n':
                page_strict = set()

        while page < page_amount:
            symbol = input("\nEnter a stock symbol to scrape:\n").lower()
            if page_strict != 0 and symbol in page_strict:
                print("Stock already scraped, try again.")
                continue
            else:
                self.start_urls.append(f'https://finance.yahoo.com/quote/{symbol}')
                page_strict.add(symbol) if page_strict != 0 else None
                page += 1

    def parse(self, response):
        items = FinanceItem()

        items['stock_name'] = response.xpath('//*[@id="quote-header-info"]/div[2]/div[1]/div[1]/h1//text()').get()
        items['previous_close'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[1]/td[2]//text()').get()
        items['open'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[2]/td[2]//text()').get()
        items['bid'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[3]/td[2]//text()').get()
        items['ask'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[4]/td[2]//text()').get()
        items['range_day'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[5]/td[2]//text()').get()
        items['range_52weeks'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[6]/td[2]//text()').get()
        items['volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[7]/td[2]//text()').get()
        items['avg_volume'] = response.xpath('//*[@id="quote-summary"]/div[1]/table/tbody/tr[8]/td[2]//text()').get()

        yield items