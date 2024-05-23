import scrapy


class MalayaspiderSpider(scrapy.Spider):
    name = "MalayaSpider"
    allowed_domains = ["malaya.com.ph"]
    start_urls = ["https://malaya.com.ph/news/"]

    def parse(self, response):
        for link in response.css('h3 a::attr(href)').getall():
            yield response.follow(link, callback=self.parse_content)
    
    def parse_content(self, response):
        box = response.css('div.td-pb-span8.td-main-content')
        yield{
            'title': box.css('h1.entry-title::text').get(),
            'author': box.css('div.td-post-author-name a::text').getall(),
            'date': box.css('span.td-post-date time::text').getall(),
            'article': box.css('div.td-post-content.tagdiv-type p::text').getall(),
            'link': response.css('link[rel="canonical"]::attr(href)').getall()

        }

        pass
