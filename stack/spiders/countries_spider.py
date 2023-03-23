import scrapy
from scrapy.selector import Selector

class CountriesSpider(scrapy.Spider):
    name = 'countries'
    start_urls = ['https://www.scrapethissite.com/pages/simple/']
    headers = ['country-name', 'country-capital', 'country-population', 'country-area']
    
    def parse(self, response, **kwargs):
        rows = response.css('div.country').getall()
        for row in rows:
            item = CountryItem()
            row = Selector(text=row)
            for header in self.headers:
                if header == 'country-name':
                    item[f"{header.replace('-', '_')}"] = row.xpath('//h3//text()').extract()[1].strip()
                    continue
                item[f"{header.replace('-', '_')}"] = row.css(f'span.{header}::text').get().strip()
            yield item
