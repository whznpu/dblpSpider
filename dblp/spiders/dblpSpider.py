import scrapy
from ..items import DblpItem 
# created by haozhewang, 2023.9.13
# | title | year | conference | authors | Bibtex

class DblpspiderSpider(scrapy.Spider):
    name = "dblpSpider"
    allowed_domains = ["dblp.org"]
    # start_urls = ["https://dblp.org"]
    start_urls=['https://dblp.org/db/']
    years=['2022','2021','2020']
    pvldb_num=['16','15','14']
    confs=['sigmod','pvldb','icde']
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
             'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
             'Accept-Encoding':'gzip, deflate, br',
             'Accept-Language':'en-US,en;q=0.9'}
    
    def start_requests(self):
        
        for i,year in enumerate(self.years):
            for conf in self.confs:
                if conf=='pvldb':
                    url=self.start_urls[0]+'journals/'+conf+'/'+conf+self.pvldb_num[i]
                else:
                    # print(self.years[i])
                    url=self.start_urls[0]+'conf/'+conf+'/'+conf+year
                    # print(url)
                print(url)
                yield scrapy.Request(url=url, headers=self.headers,callback=self.parse,cb_kwargs=dict(year=year,conf=conf))     
            
            
    
    def parse(self, response,year:str,conf:str):
        # print(response.body)
        # with open("test.html","w") as html_file:
        #     html_file.write(str(response.body))
        items=[]
        titles=response.xpath("//div[@id='main']/ul[@class='publ-list']/li/cite")
        for title in titles:
            
            item=DblpItem()
            # multiple authors combined into one string
            item['authors']=title.xpath("span[@itemprop='author']//text()").extract()
            item['year']=year
            item['conf']=conf
            item['title']=title.xpath("span[@class='title']/text()").extract()
        
            print(item['title'])
            items.append(item)
        
        return items
        # pass
