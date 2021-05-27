# href-scraper
Utilizing Scarpy framework in Python, I developed a simple/automated script that will pull ```href``` tag values and store them into a json file 

## Requisites
- Python3: https://www.python.org/downloads/
- pip install virtualenv

## How-to
1. git clone https://github.com/p-cap/href-scraper.git
2. chmod 700 href_scraper
3. Edit the ```href_spider.py``` file and adding the desired URL
   ```
    ...
    class HrefSpider(scrapy.Spider):
       name = 'href_links'
    
      # makes requests to the urls defined inside the given variable
    start_urls = [ 
       #>>> Insert URL here <<<#
    ]
    ...
   ```
4. ./href_scraper
5. open ```href_links.json``` to see what's links were grabbed
