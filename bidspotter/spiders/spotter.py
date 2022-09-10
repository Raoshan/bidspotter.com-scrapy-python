import scrapy
import pandas as pd
df = pd.read_csv('F:\Web Scraping\Golabal\keywords.csv')
base_url = 'https://www.bidspotter.com/en-us/search-results?searchTerm={}'

class SpotterSpider(scrapy.Spider):
    name = 'spotter'
    
    def start_requests(self):
        for index in df:
            yield scrapy.Request(base_url.format(index), cb_kwargs={'index':index})

    def parse(self, response, index):
        links = response.css("[name='lot-title']::attr(href)")
        for link in links:
            yield response.follow("https://www.bidspotter.com"+link.get(), callback=self.parse_item, cb_kwargs={'index':index})  

        next_page = response.css("ul.pagination-content")
        print(".....")  
        print(next_page)  
        print(".....")      
          
    def parse_item(self, response, index): 
        print(".................")  
        product_url = response.url
        print(product_url)
        item_type=index.strip()
        print(item_type)
        image_link = response.css('div.image img::attr(src)').get()
        print(image_link)
        auction_date = response.css('span.data time time::text').get()
        print(auction_date)
        location = response.xpath("//*[@class='Rtable-cell Rtable-cell--2of3 Rtable-cell--rowEnd']/strong/span/text()").get()
        print(location)
        product_name = response.css('h2.header::text').get()
        print(product_name)
        lot_number = response.css('p.lot-number::text').get().strip()
        print(lot_number)
        auctioner = response.css('p.ui.header::text').get()
        print(auctioner)
       

        
