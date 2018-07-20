import scrapy
from tutorial.items import AuthorItem

class AuthorSpider(scrapy.Spider):
    name='author'
    start_urls = ['http://quotes.toscrape.com/']
    items=[]
    def parse(self, res):
        self.items=[]
        for href in res.css('.author + a::attr(href)'):
            yield res.follow(href,self.parse_author)            
        for href in res.css('li.next a::attr(href)'):
            yield res.follow(href,self.parse)

        return self.items
    def parse_author(self,res):
        def extract_with_css(quey):
            return res.css(quey).extract_first().strip()
        
        item=AuthorItem()
        n=extract_with_css('h3.author-title::text')
        b=extract_with_css('.author-born-date::text')
        d=extract_with_css('.author-description::text')
        item['name']=n
        item['date']=b
        item['desc']=d
        self.items.append(item)
        yield item