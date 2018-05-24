#-*- coding: utf8 -*-
import scrapy
from bloomfilter import BloomFilter
from random import shuffle

class newsSpider(scrapy.Spider):
    name = "news"
    start_urls = [
        'http://www.bbc.com/news',
    ]
    count = 0
    n = 2000 #Number of bits
    p = 0.15 #falseProbabilityRate
    bloomf = BloomFilter(2000,0.15)
 
    def parse(self, response,count=1):
	
	
	mydiv = response.xpath('//div')
	for p in mydiv.xpath('.//p/text()').extract():
		p=p.replace(u"Â", u"").replace(u"â", u"")
		if 'Email' in p or 'MMS' in p or 'Follow' in p or 'stories' in p or 'news' in p or 'world' in p:
			continue

		yield {
			'text': p
                 }
	newsSpider.count = newsSpider.count + 1
	if newsSpider.count <=5:
       		 URLlist = response.css('div a::attr("href")').extract()         
		 for next_page in URLlist:
			if self.bloomf.check(next_page):
				continue
			self.bloomf.add(next_page)
	    	 	newsSpider.count = newsSpider.count + 1
	    	 	if newsSpider.count >= 5:
				break
            	 	yield response.follow(next_page, self.parse)
	

