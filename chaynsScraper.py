import scrapy
from scrapy_splash import SplashRequest


class ChaynsSpider(scrapy.Spider):
    name = 'chayns_spider'
    start_urls = ['https://mvv.chayns.net?ts=98', 'https://tobit.software']
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 5, 'timeout': 10}, endpoint='render.html')

    #def parse_iframe(self, response):
      #  print(response.text)

    def parse(self, response):
        TITLE_SELECTOR = './/title/text()'
        PAGE_NAME_SELECTOR = './/meta[@name = "og:title"]/@content'
        IFRAME_SELECTOR = './/iframe/@src'

        page_name = response.xpath(PAGE_NAME_SELECTOR)[0].extract()
        title = response.xpath(TITLE_SELECTOR).extract_first()
        title = title.replace(page_name, '')
        title = title.replace('|', '')
        title = title.strip()
        iframe_url = response.xpath(IFRAME_SELECTOR).extract_first()
        yield {
            'title': title,
            'pageName': page_name,
            'iframeUrl': iframe_url,
            'text': response.text,
        }

       # yield SplashRequest(url=iframe_url, callback=self.parse_iframe, endpoint='render.html')
