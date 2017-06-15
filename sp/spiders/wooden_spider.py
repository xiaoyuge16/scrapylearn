from scrapy.spider import Spider


class BlogSpider(Spider):
    name = "woodenrobot"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        'https://woodenrobot.me'
    ]
def parse(self, response):
    titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
    for title in titles:
        print title.strip()

