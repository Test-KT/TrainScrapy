# -*- coding: UTF-8 -*-
import scrapy
from tutorial.items import NewsItem

class NewsSpider(scrapy.Spider):
    name="News"
    start_urls=['http://weixin.sogou.com']


    def parse(self,res):
        # news_href_list=res.xpath('//ul[@class="news-list"]/li/div[2]/h3/a/@href')
        # for herf in news_href_list:
        #     url=res.urljoin(herf.extract())
            self.logger.debug(url)
        items=[]
        newbox=res.css("ul.news-list")
        for item in newbox.css('li'):
            it=NewsItem()
            title=item.css('div.txt-box h3 a::text').extract()
            info=item.css('div.txt-box p.txt-info::text').extract()
            post_user=item.css('div.txt-box div.s-p a::text').extract()
            time=item.css('div.txt-box div.s-p span::attr(t)').extract()
            it['title']=title
            it['info']=info
            it['time']=time
            it['post_user']=post_user
            items.append(it)

            yield it

        return items
    


            
            
