# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest

lua_script = '''
function main(splash)
    splash:go(splash.args.url)
    splash:wait(2)
    splash:runjs("document.getElementByClassName('page')[0].scrollIntoView(true)")
    splash:wait(2)
    return splash:html()
end
'''


class JdBookSpider(scrapy.Spider):
    name = 'jd_book'
    #allowed_domains = ['search.js.com']
    #start_urls = ['http://search.js.com/']
    base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&book=y&wq=python'

    def start_requests(self):
        yield  Request(self.base_url,callback=self.parse_url,dont_filter=True)
    
    def parse_url(self,response):
        total_page = int(response.css('span.fp-text i::text').extract_first())
        for page in range(total_page):
            this_page = page*2
            url = self.base_url+'&page='+str(this_page)

            yield SplashRequest(
                url,
                callback=self.parse,
                endpoint='execute',
                args={'lua_source':lua_script,'image':0,},
                cache_args=['lua_source'])
    def parse(self, response):
        sel = response.css('ul.gl-warp.clearfix li.gl-item')
        for book in sel:
            name = book.css('.p-name em::text').extract_first()
            price = book.css('.p-price i::text').extract_first()
            publish = book.css('.p-shopnum a::text').extract_first()
            commit = book.css('.p-commit a::text').extract_first()
            yield {
                'name':     name,
                'price':    price,
                'pulish':   publish,
                'commit':   commit,
            }


