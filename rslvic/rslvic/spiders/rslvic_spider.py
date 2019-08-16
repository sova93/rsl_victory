import scrapy
from scrapy_splash import SplashRequest
import js2xml

class RslvicSpider(scrapy.Spider):
    name = 'RslvicSpider'
    allowed_domains = ['www.rslvic.com.au']

    def start_requests(self):
        yield SplashRequest(
            url='http://www.rslvic.com.au/rsl-network/victorian-map-of-all-branches/',
            callback=self.parse,
        )

    def parse(self, response):
        jstree = js2xml.parse(response.xpath('//script/text()').extract_first())
        for el in jstree.xpath('//functioncall/arguments/object'):
            yield js2xml.jsonlike.make_dict(el)