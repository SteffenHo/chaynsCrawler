import scrapy

class ChaynsSpider(scrapy.Spider):
    name = 'chayns_spider'
    start_urls = ['https://mvv.chayns.net/']

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
            'iframeUrl': response.xpath(IFRAME_SELECTOR).extract_first(),
            'body': response.body.decode(response.encoding)
        }

        #yield (scrapy.Request(iframeUrl, callback=self.parse_iframe))

   # def parse_iframe(self, response):
    #    yield response
