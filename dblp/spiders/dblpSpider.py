import scrapy
from ..items import DblpItem 
# created by haozhewang, 2023.9.13
# | title | year | conference | authors | Bibtex

class DblpspiderSpider(scrapy.Spider):
    name = "dblpSpider"
    allowed_domains = ["dblp.org"]
    # start_urls = ["https://dblp.org"]
    start_urls=['https://dblp.org/db/conf/']
    years=['2022']
    confs=['sigmod']
    
    def start_requests(self):
        
        for year in self.years:
            for conf in self.confs:
                url=self.start_urls[0]+conf+'/'+conf+year
                print(url)
                yield scrapy.Request(url=url,callback=self.parse,cb_kwargs=dict(year=year,conf=conf))     

    def parse(self, response,year:str,conf:str):
        # print(response.body)
        with open("test.html","w") as html_file:
            html_file.write(str(response.body))
        items=[]
        titles=response.xpath("//div[@id='main']/ul[@class='publ-list']/li/cite")
        print(titles)
        for title in titles:
            
            item=DblpItem()
            item['year']=year
            item['conf']=conf
            item['title']=title.xpath("span[@class='title']/text()").extract()
        
            items.append(item)
        
        return items
        # pass
