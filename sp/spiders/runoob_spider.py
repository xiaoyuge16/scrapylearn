# coding=utf-8

from scrapy.spider import Spider
from sp.items import RunoobItem


class RunoobSpider(Spider):
    name = "runoob"
    allowed_domains = ["runoob.com"]
    start_urls = [
        "http://www.runoob.com"
    ]

    # def parse(self, response):
    #     H2 = response.selector.xpath('//h2/text()').extract()
    #     for h2 in H2:
    #         print h2.strip('')
    #     H4 = response.xpath('//h4').extract()
    #     for h4 in H4:
    #         print "这是标题4:",
    #         print h4.strip('</h4>')
    #     with open('runoob.html','wb') as f:
    #         f.write(response.body)
    #     self.log('Saved file runoob.txt')

    def parse(self, response):
        items = RunoobItem()
        # items['h2'] = response.selector.xpath('//h2/text()').extract()
        # items['h4'] = response.xpath('//h4').extract()
        items['link'] = response.css("ul > li > a::attr('href')").extract()
        items['atitle'] = response.css("ul > li > a::attr('title')").extract()
        yield items
        with open('runoob.html','wb') as f:
            f.write(response.body)
        self.log('Saved file runoob.html')
