# -*- coding: utf-8 -*-
import scrapy
# 导入爬取规则 rules 字段用
from scrapy.linkextractors import LinkExtractor
# 导入父类CrawlSpider 和字段Rule
from scrapy.spiders import CrawlSpider, Rule
# 导入item
from properties.items import PropertiesItem
# 导入item 装饰器
from scrapy.loader import ItemLoader
# 导入装饰器处理函数
from scrapy.loader.processors import MapCompose, Join
# 导入bs4页面解析库
from bs4 import BeautifulSoup
# 导入时间库
import datetime

class BasicSpider(scrapy.Spider):
    name = 'basic'
    # allowed_domains = ['exploit-db']
    start_urls = ['https://0day.today/']

    
    def parse(self, response):
        Cookie1 = response.headers.getlist('Set-Cookie')   #查看一下响应Cookie，也就是第一次访问注册页面时后台写入浏览器的Cookie
        print(Cookie1)
        soup = BeautifulSoup(response.body,"html.parser")
        print(soup.prettify())

        # print(response.url)
        # soup = BeautifulSoup(response.body, "html.parser")
        # print(soup.prettify())
        # link = LinkExtractor(restrict_xpaths='//a[@class="PreviewTooltip"]')
        # links = link.extract_links(response)
        # print(links)

        # 定义loader 装饰器
        # loader = ItemLoader(item=PropertiesItem(), response=response)

        # loader.add_value('link', response.url)

        # loader.add_value('text', response.body.decode('utf-8'))

        # loader.add_xpath('text', 'xpath表达式', MapCompose(unicode.strip, unicode.titile), Join())

        # return loader.load_item()
        print("*" * 40)
        # print("response text: %s" % response.text)
        print("response headers: %s" % response.headers)
        print("response meta: %s" % response.meta)
        print("request headers: %s" % response.request.headers)
        print("request cookies: %s" % response.request.cookies)
        print("request meta: %s" % response.request.meta)