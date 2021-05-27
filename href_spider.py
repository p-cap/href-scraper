import sys
import scrapy


class HrefSpider(scrapy.Spider):
    name = 'href_links'
    
    # makes requests to the urls defined inside the given variable
    start_urls = [ 
       'https://www.twilio.com/login?g=%2Fconsole%3F&t=2b1c98334b25c1a785ef15b6556396290e3c704a9b57fc40687cbccd79c46a8c',
    ]   
   
    # called the default callback
    def parse(self, response):
        # loop through the quote elements using a CSS Selector
        for api in response.css('a'):
            # yield a Python dict
            yield {
                'APIs': api.attrib['href']
            }   


