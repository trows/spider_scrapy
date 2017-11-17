import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from spider_scrapy.items import SpiderScrapyItem


class CCGPSpider(scrapy.Spider):
    name = 'CCGP'
    allowed_domain = ['ccgp-beijing.gov.cn']
    base_url = 'http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg/'
    base_url_start = base_url + 'index'
    base_url_end = '.html'

    def start_requests(self):
        yield Request(self.base_url_start + self.base_url_end)
        for i in range(1, 1):
            url = self.base_url_start + str(i) + self.base_url_end
            yield Request(url, callback=self.parse)

    def parse(self, response):
        document = BeautifulSoup(response.text, 'lxml')
        for link in document.find_all('li'):
            url = self.base_url + link.a.get('href')[2:]
            print(url)
            yield Request(url, callback=self.get_content)

    def get_content(self, response):
        document = BeautifulSoup(response.text, 'lxml')

        document.find('strong', text='项目名称')

        pass
