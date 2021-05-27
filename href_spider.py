import scrapy

class HrefSpider(scrapy.Spider):
    name = 'href_links'
    
    # makes requests to the urls defined inside the given variable
    start_urls = [ 
       #>>> Insert URL here <<<#
    ]   

    # called the default callback
    def parse(self, response):
        
        # loop through the a elements 
        for api in response.css('a'):
            # yield a Python dict
            yield {
                'APIs': api.attrib['href']
            }   
