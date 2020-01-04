import scrapy
from scrapy_splash import SplashRequest


class MySpider(scrapy.Spider):
    name = "jsscraper"

    start_urls = ["http://mvv.chayns.net"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, endpoint='render.html')

    def parse(self, response):
        print('test')
        print(response.text)
        #for q in response.css("div.quote"):
         #   yield {
          #      "author": q.css(".author::text").extract_first(),
           #     "quote": q.css(".text::text").extract_first()
           # }
