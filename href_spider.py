import sys
import scrapy


class HrefSpider(scrapy.Spider):
    name = 'href_links'
    
    # makes requests to the urls defined inside the given variable
    start_urls = [ 
       #Enter URL to scrape here
    ]   
   
    # called the default callback
    def parse(self, response):
        # loop through the quote elements using a CSS Selector
        for api in response.css('a'):
            # yield a Python dict
            yield {
                'APIs': api.attrib['href']
            }   


