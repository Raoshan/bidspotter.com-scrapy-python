import scrapy
import pandas as pd
df = pd.read_csv('F:\Web Scraping\Golabal\keywords.csv')
base_url = 'https://www.bidspotter.com/en-us/search-results?searchTerm={}'

class BidSpider(scrapy.Spider):
    name = 'bid'
   
    def start_requests(self):
        for index in df:
            yield scrapy.Request(base_url.format(index), cb_kwargs={'index':index})

    def parse(self, response,index):
        
        items = response.css('.lot-single')
        for item in items:
            name = item.css('.lot-title::text').get()
            print(name)
            item_type = index.strip()
            print(item_type)            
            lot_number = item.css('.lot-number::text').get()
            print(lot_number)            
            try:
                auction_date=item.css(".date strong::text").get()               
                print(auction_date)
            except:
                auction_date = ""
                print(auction_date)    
    
            location = item.xpath("//span[@class='lotlocation']/strong/text()").get()
            print(location)
            auctioner = item.css('.byline::text').get()
            print(auctioner)
            link = response.urljoin(item.css('a::attr(href)').get())
            print(link)
            image_link = response.urljoin(item.css("img::attr(src)").get())
           
            print(image_link)
            

       

     
            

     