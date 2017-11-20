import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from scrapy.utils.response import get_base_url
from spider_scrapy.items import SpiderScrapyItem


class CCGPSpider(scrapy.Spider):
    name = 'CCGP'
    allowed_domain = ['ccgp-beijing.gov.cn']
    base_url = 'http://www.ccgp-beijing.gov.cn/xxgg/sjzfcggg/sjzbgg/'
    base_url_start = base_url + 'index_'
    base_url_end = '.html'

    def start_requests(self):
        yield Request(self.base_url_start + self.base_url_end,callback=self.parse)
        for i in range(1, 16):
            url = self.base_url_start + str(i) + self.base_url_end
            yield Request(url, callback=self.parse)

    def parse(self, response):
        document = BeautifulSoup(response.text, 'lxml')
        for link in document.find_all('li'):
            url = self.base_url + link.a.get('href')[2:]
            print(url)
            yield Request(url, callback=self.get_content)

    def get_content(self, response):
        item = SpiderScrapyItem()
        document = BeautifulSoup(response.text, 'lxml')
        item['url'] = get_base_url(response)
        item['name'] = document.find('strong', text=re.compile('项目名称')).parent.get_text()[5:]
        title = document.find('div', class_='div_hui').find_next('div').find('span').get_text()
        item['type'] = title[1:3]
        item['title'] = title[4:]
        item['code'] = document.find('strong', text=re.compile('项目编号')).parent.get_text()[5:]
        return item
