import scrapy
import json
from  tutorial.items import QuotesItem
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/',
        # 'http://quotes.toscrape.com/page/2/',
    ]
    # def start_requests(self):
    #     urls=[
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #         ]
    #     for url in urls:
    #         yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, res):
        page = res.url.split("/")[-2]
        filename = 'quotes-%s.json' % page

        # 抓取感兴趣的内容
        # list=[]
        items=[]
        for qute in res.css('div.quote'):
            item=QuotesItem()
            item['title']=qute.css('span.text::text').extract_first()
            item['author']=qute.css('small.author::text').extract_first()
            item['tags']=qute.css('div.tags a.tag::text').extract()
            item['link']=qute.css('span a::attr(href)').extract_first()
            items.append(item)
            yield item
        

        # next_page=res.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
            # next_page=res.urljoin(next_page)
            # yield scrapy.Request(next_page,callback=self.parse)

        for a in res.css('li.next a::attr(href)'):
            yield res.follow(a,callback=self.parse)
        # 保存到文件中
        # self.writeFile(filename,list)
        return items


        


    def writeFile(self,filename,list):
        """
        写入文件中
        """
        with open(filename,'w') as f:
            for li in list:
                str=json.dumps(li)
                f.write(str)
                f.write('\n')
        self.log('save file %s'%filename)
